"""Memory addresses for Pokémon Red/Blue (English version)."""

# Party Pokémon
PARTY_COUNT = 0xD163  # Number of Pokémon in party (0-6)
PARTY_SPECIES = 0xD164  # Species IDs (6 bytes, terminated by 0xFF)
PARTY_DATA_START = 0xD16B  # First Pokémon data (44 bytes each)

# Pokémon data structure offsets (from PARTY_DATA_START + slot*44)
POKEMON_SPECIES = 0x00      # Species ID (1 byte)
POKEMON_HP_CURRENT = 0x01   # Current HP (2 bytes, big-endian)
POKEMON_LEVEL_BOX = 0x03    # Level when in box (1 byte)
POKEMON_STATUS = 0x04       # Status condition (1 byte)
POKEMON_TYPE1 = 0x05        # Type 1 (1 byte)
POKEMON_TYPE2 = 0x06        # Type 2 (1 byte)
POKEMON_MOVE1 = 0x08        # Move 1 ID (1 byte)
POKEMON_MOVE2 = 0x09        # Move 2 ID (1 byte)
POKEMON_MOVE3 = 0x0A        # Move 3 ID (1 byte)
POKEMON_MOVE4 = 0x0B        # Move 4 ID (1 byte)
POKEMON_LEVEL = 0x21        # Actual level (1 byte, offset 33)
POKEMON_HP_MAX = 0x22       # Max HP (2 bytes, big-endian)
POKEMON_ATTACK = 0x24       # Attack stat (2 bytes, big-endian)
POKEMON_DEFENSE = 0x26      # Defense stat (2 bytes, big-endian)
POKEMON_SPEED = 0x28        # Speed stat (2 bytes, big-endian)
POKEMON_SPECIAL = 0x2A      # Special stat (2 bytes, big-endian)

# Pokédex
POKEDEX_OWNED = 0xD2F7  # Bitfield of owned Pokémon (19 bytes)
POKEDEX_SEEN = 0xD30A   # Bitfield of seen Pokémon (19 bytes)

# Player
PLAYER_NAME = 0xD158  # Player name (up to 11 bytes, terminated by 0x50)
PLAYER_X = 0xD362     # X coordinate
PLAYER_Y = 0xD361     # Y coordinate
MAP_ID = 0xD35E       # Current map ID
BADGES = 0xD356       # Badge bitfield
MONEY = 0xD347        # Money (3 bytes, BCD format)

# Play time
PLAY_TIME_HOURS = 0xDA40    # Hours (2 bytes, big-endian)
PLAY_TIME_MINUTES = 0xDA42  # Minutes (1 byte)
PLAY_TIME_SECONDS = 0xDA44  # Seconds (1 byte)

# Battle
IN_BATTLE = 0xD057           # 0 = not in battle, >0 = in battle
WILD_POKEMON_SPECIES = 0xCFE5  # Wild Pokémon species ID
WILD_POKEMON_LEVEL = 0xCFE6    # Wild Pokémon level
