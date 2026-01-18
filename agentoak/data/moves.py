"""Move names for Pokémon Red/Blue."""

import json
from pathlib import Path

# Load move data from JSON
_data_file = Path(__file__).parent / "moves_gen1.json"
with open(_data_file) as f:
    _MOVE_DATA = json.load(f)

# Convert keys to int
MOVE_NAMES = {int(k): v for k, v in _MOVE_DATA.items()}


def get_move_name(move_id: int) -> str:
    """Get move name from ID."""
    return MOVE_NAMES.get(move_id, f"Move #{move_id}")
