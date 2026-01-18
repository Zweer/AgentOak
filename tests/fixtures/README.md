# Test Fixtures

This directory contains save states and their specifications for testing.

## Structure

Each test save consists of two files:
- `{name}.state` - PyBoy save state file
- `{name}.json` - Test specification with expected values

## Available Test Saves

### bulbasaur
- **Description**: Starter Bulbasaur in Oak's Lab
- **Location**: Oak's Lab (Map 40, position 5,6)
- **Party**: 1 Bulbasaur, Level 5
- **Moves**: Tackle, Growl
- **Badges**: 0

## Adding New Test Saves

1. Create the save state using `scripts/play_manual.py`
2. Move it to `tests/fixtures/{name}.state`
3. Create `tests/fixtures/{name}.json` with the specification:

```json
{
  "description": "Brief description",
  "player": {
    "map_id": 40,
    "map_name": "Oak's Lab",
    "x": 5,
    "y": 6,
    "badges": 0
  },
  "party": [
    {
      "species_id": 153,
      "name": "Bulbasaur",
      "level": 5,
      "current_hp": 21,
      "max_hp": 21,
      "attack": 10,
      "defense": 10,
      "speed": 10,
      "special": 12,
      "moves": [33, 45, 0, 0],
      "move_names": ["Tackle", "Growl", null, null],
      "ivs": {
        "attack": {"min": 0, "max": 15},
        "defense": {"min": 0, "max": 15},
        "speed": {"min": 0, "max": 15},
        "special": {"min": 0, "max": 15}
      }
    }
  ],
  "pokedex": {
    "owned": 0
  },
  "collision": {
    "has_walkable_tiles": true,
    "has_blocked_tiles": true
  }
}
```

4. Add the name to `SAVE_STATES` list in `tests/test_memory_reading.py`
5. Run `make test` to verify

The tests will automatically run against all save states in the list!
