"""Memory addresses for Pokémon Red/Blue (English version)."""

# Party Pokémon
PARTY_COUNT = 0xD163  # Number of Pokémon in party (0-6)
PARTY_SPECIES = 0xD164  # Species IDs (6 bytes, terminated by 0xFF)
PARTY_DATA_START = 0xD16B  # First Pokémon data (44 bytes each)

# Pokédex
POKEDEX_OWNED = 0xD2F7  # Bitfield of owned Pokémon (19 bytes)
POKEDEX_SEEN = 0xD30A  # Bitfield of seen Pokémon (19 bytes)

# Player
PLAYER_X = 0xD362  # X coordinate
PLAYER_Y = 0xD361  # Y coordinate
MAP_ID = 0xD35E  # Current map ID
BADGES = 0xD356  # Badge bitfield

# Battle
IN_BATTLE = 0xD057  # 0 = not in battle, >0 = in battle
WILD_POKEMON_SPECIES = 0xCFE5  # Wild Pokémon species ID
WILD_POKEMON_LEVEL = 0xCFE6  # Wild Pokémon level
