"""Memory reading utilities for Pokémon Red/Blue."""

from dataclasses import dataclass

from agentoak.emulator import GameBoyEmulator
from agentoak.memory import addresses


@dataclass
class PartyPokemon:
    """Data for a Pokémon in the party."""
    species_id: int
    level: int
    current_hp: int
    max_hp: int
    attack: int
    defense: int
    speed: int
    special: int
    moves: list[int]  # List of 4 move IDs
    # IVs (Individual Values, 0-15 each)
    attack_iv: int
    defense_iv: int
    speed_iv: int
    special_iv: int


def read_party_count(emulator: GameBoyEmulator) -> int:
    """Read number of Pokémon in party."""
    return emulator.read_memory(addresses.PARTY_COUNT)[0]


def read_party_pokemon(emulator: GameBoyEmulator, slot: int) -> PartyPokemon | None:
    """Read Pokémon data from party slot (0-5).
    
    Args:
        emulator: GameBoy emulator instance
        slot: Party slot (0-5)
        
    Returns:
        PartyPokemon or None if slot is empty
    """
    party_count = read_party_count(emulator)
    if slot >= party_count:
        return None
    
    # Each Pokémon is 44 bytes
    base_addr = addresses.PARTY_DATA_START + (slot * 44)
    
    # Read Pokémon data structure
    data = emulator.read_memory(base_addr, 44)
    
    species_id = data[addresses.POKEMON_SPECIES]
    current_hp = (data[addresses.POKEMON_HP_CURRENT] << 8) | data[addresses.POKEMON_HP_CURRENT + 1]
    level = data[addresses.POKEMON_LEVEL]
    max_hp = (data[addresses.POKEMON_HP_MAX] << 8) | data[addresses.POKEMON_HP_MAX + 1]
    attack = (data[addresses.POKEMON_ATTACK] << 8) | data[addresses.POKEMON_ATTACK + 1]
    defense = (data[addresses.POKEMON_DEFENSE] << 8) | data[addresses.POKEMON_DEFENSE + 1]
    speed = (data[addresses.POKEMON_SPEED] << 8) | data[addresses.POKEMON_SPEED + 1]
    special = (data[addresses.POKEMON_SPECIAL] << 8) | data[addresses.POKEMON_SPECIAL + 1]
    
    moves = [
        data[addresses.POKEMON_MOVE1],
        data[addresses.POKEMON_MOVE2],
        data[addresses.POKEMON_MOVE3],
        data[addresses.POKEMON_MOVE4],
    ]
    
    # IVs are stored at offset 0x1B and 0x1C (27 and 28)
    # Format: AAAA DDDD SSSS SSSS (Attack, Defense, Speed, Special)
    # Each IV is 4 bits (0-15)
    iv_byte1 = data[0x1B]  # Attack (high 4 bits) + Defense (low 4 bits)
    iv_byte2 = data[0x1C]  # Speed (high 4 bits) + Special (low 4 bits)
    
    attack_iv = (iv_byte1 >> 4) & 0xF
    defense_iv = iv_byte1 & 0xF
    speed_iv = (iv_byte2 >> 4) & 0xF
    special_iv = iv_byte2 & 0xF
    
    return PartyPokemon(
        species_id=species_id,
        level=level,
        current_hp=current_hp,
        max_hp=max_hp,
        attack=attack,
        defense=defense,
        speed=speed,
        special=special,
        moves=moves,
        attack_iv=attack_iv,
        defense_iv=defense_iv,
        speed_iv=speed_iv,
        special_iv=special_iv,
    )


def read_full_party(emulator: GameBoyEmulator) -> list[PartyPokemon]:
    """Read all Pokémon in party."""
    party_count = read_party_count(emulator)
    return [
        read_party_pokemon(emulator, i)
        for i in range(party_count)
        if read_party_pokemon(emulator, i) is not None
    ]


def read_pokedex_owned_count(emulator: GameBoyEmulator) -> int:
    """Count total owned Pokémon in Pokédex."""
    data = emulator.read_memory(addresses.POKEDEX_OWNED, 19)
    return sum(bin(byte).count("1") for byte in data)


def is_pokemon_owned(emulator: GameBoyEmulator, pokedex_num: int) -> bool:
    """Check if a Pokémon is owned (1-indexed).
    
    Args:
        emulator: GameBoy emulator instance
        pokedex_num: Pokédex number (1-151)
        
    Returns:
        True if owned, False otherwise
    """
    if not 1 <= pokedex_num <= 151:
        raise ValueError(f"Invalid Pokédex number: {pokedex_num}")
    
    byte_index = (pokedex_num - 1) // 8
    bit_index = (pokedex_num - 1) % 8
    
    data = emulator.read_memory(addresses.POKEDEX_OWNED + byte_index, 1)
    return bool(data[0] & (1 << bit_index))


def read_player_position(emulator: GameBoyEmulator) -> tuple[int, int, int]:
    """Read player position.
    
    Returns:
        Tuple of (map_id, x, y)
    """
    map_id = emulator.read_memory(addresses.MAP_ID)[0]
    x = emulator.read_memory(addresses.PLAYER_X)[0]
    y = emulator.read_memory(addresses.PLAYER_Y)[0]
    return (map_id, x, y)


def read_badge_count(emulator: GameBoyEmulator) -> int:
    """Count number of badges obtained."""
    badges = emulator.read_memory(addresses.BADGES)[0]
    return bin(badges).count("1")


def read_player_name(emulator: GameBoyEmulator) -> str:
    """Read player name."""
    name_bytes = emulator.read_memory(addresses.PLAYER_NAME, 11)
    
    # Character map (simplified, common chars)
    char_map = {
        0x80: "A", 0x81: "B", 0x82: "C", 0x83: "D", 0x84: "E", 0x85: "F", 0x86: "G",
        0x87: "H", 0x88: "I", 0x89: "J", 0x8A: "K", 0x8B: "L", 0x8C: "M", 0x8D: "N",
        0x8E: "O", 0x8F: "P", 0x90: "Q", 0x91: "R", 0x92: "S", 0x93: "T", 0x94: "U",
        0x95: "V", 0x96: "W", 0x97: "X", 0x98: "Y", 0x99: "Z",
        0xA0: "a", 0xA1: "b", 0xA2: "c", 0xA3: "d", 0xA4: "e", 0xA5: "f", 0xA6: "g",
        0xA7: "h", 0xA8: "i", 0xA9: "j", 0xAA: "k", 0xAB: "l", 0xAC: "m", 0xAD: "n",
        0xAE: "o", 0xAF: "p", 0xB0: "q", 0xB1: "r", 0xB2: "s", 0xB3: "t", 0xB4: "u",
        0xB5: "v", 0xB6: "w", 0xB7: "x", 0xB8: "y", 0xB9: "z",
    }
    
    result = []
    for byte in name_bytes:
        if byte == 0x50:  # Terminator
            break
        result.append(char_map.get(byte, "?"))
    return "".join(result)


def read_money(emulator: GameBoyEmulator) -> int:
    """Read money (BCD format)."""
    money_bytes = emulator.read_memory(addresses.MONEY, 3)
    b1, b2, b3 = money_bytes
    return (b1 >> 4) * 100000 + (b1 & 0xF) * 10000 + (b2 >> 4) * 1000 + (b2 & 0xF) * 100 + (b3 >> 4) * 10 + (b3 & 0xF)


def read_play_time(emulator: GameBoyEmulator) -> dict[str, int]:
    """Read play time."""
    time_bytes = emulator.read_memory(addresses.PLAY_TIME_HOURS, 5)
    hours = (time_bytes[0] << 8) | time_bytes[1]
    minutes = time_bytes[2]
    seconds = time_bytes[3]
    return {"hours": hours, "minutes": minutes, "seconds": seconds}
