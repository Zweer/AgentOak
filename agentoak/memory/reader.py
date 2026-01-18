"""Memory reading utilities for Pokémon Red/Blue."""

from agentoak.emulator import GameBoyEmulator
from agentoak.memory import addresses


def read_party_count(emulator: GameBoyEmulator) -> int:
    """Read number of Pokémon in party."""
    return emulator.read_memory(addresses.PARTY_COUNT)[0]


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
