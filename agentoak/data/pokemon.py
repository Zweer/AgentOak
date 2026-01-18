"""Pokémon species data."""

import json
from pathlib import Path

# Load Pokemon data from JSON
_data_file = Path(__file__).parent / "pokemon_gen1.json"
with open(_data_file) as f:
    _POKEMON_DATA = json.load(f)

# Convert keys to int and create lookup dict
POKEMON_NAMES = {int(k): v["name"] for k, v in _POKEMON_DATA.items()}


def get_pokemon_name(species_id: int) -> str:
    """Get Pokémon name from internal species ID."""
    return POKEMON_NAMES.get(species_id, f"Unknown #{species_id}")
