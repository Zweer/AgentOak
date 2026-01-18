"""Test memory reading with real save state."""

import json
from pathlib import Path

import pytest

from agentoak.data import get_map_name, get_move_name, get_pokemon_name
from agentoak.emulator import GameBoyEmulator
from agentoak.memory import read_badge_count, read_full_party, read_player_position


def load_test_spec(name: str) -> dict:
    """Load test specification JSON."""
    spec_path = Path(__file__).parent / "fixtures" / f"{name}.json"
    with open(spec_path) as f:
        return json.load(f)


def load_save_state(name: str) -> GameBoyEmulator:
    """Load a save state by name."""
    emu = GameBoyEmulator("roms/pokemon-blue.gb", headless=True)
    save_path = Path(__file__).parent / "fixtures" / f"{name}.state"
    emu.load_state(str(save_path))
    emu.tick(60)  # Let it settle
    return emu


# Parametrize tests with all available save states
SAVE_STATES = ["bulbasaur"]  # Add more as we create them


@pytest.fixture(params=SAVE_STATES)
def save_state(request):
    """Load save state and its spec."""
    name = request.param
    spec = load_test_spec(name)
    emu = load_save_state(name)
    yield emu, spec
    emu.close()


def test_player_position(save_state):
    """Test reading player position."""
    emu, spec = save_state
    expected = spec["player"]
    
    map_id, x, y = read_player_position(emu)
    
    assert map_id == expected["map_id"], f"Map ID should be {expected['map_id']}"
    assert x == expected["x"], f"X coordinate should be {expected['x']}"
    assert y == expected["y"], f"Y coordinate should be {expected['y']}"
    
    # Test map name
    map_name = get_map_name(map_id)
    assert map_name == expected["map_name"]


def test_badges(save_state):
    """Test reading badge count."""
    emu, spec = save_state
    expected = spec["player"]["badges"]
    
    badges = read_badge_count(emu)
    assert badges == expected, f"Should have {expected} badges"


def test_party_pokemon(save_state):
    """Test reading party Pokémon data."""
    emu, spec = save_state
    expected_party = spec["party"]
    
    party = read_full_party(emu)
    
    assert len(party) == len(expected_party), f"Should have {len(expected_party)} Pokémon"
    
    for i, (pokemon, expected) in enumerate(zip(party, expected_party)):
        # Test species
        assert pokemon.species_id == expected["species_id"], \
            f"Pokemon {i}: species_id mismatch"
        assert get_pokemon_name(pokemon.species_id) == expected["name"], \
            f"Pokemon {i}: name mismatch"
        
        # Test level and HP
        assert pokemon.level == expected["level"], f"Pokemon {i}: level mismatch"
        assert pokemon.current_hp == expected["current_hp"], f"Pokemon {i}: current_hp mismatch"
        assert pokemon.max_hp == expected["max_hp"], f"Pokemon {i}: max_hp mismatch"
        
        # Test stats
        assert pokemon.attack == expected["attack"], f"Pokemon {i}: attack mismatch"
        assert pokemon.defense == expected["defense"], f"Pokemon {i}: defense mismatch"
        assert pokemon.speed == expected["speed"], f"Pokemon {i}: speed mismatch"
        assert pokemon.special == expected["special"], f"Pokemon {i}: special mismatch"
        
        # Test IVs (exact values for regression testing)
        iv_spec = expected["ivs"]
        assert pokemon.attack_iv == iv_spec["attack"], f"Pokemon {i}: attack IV mismatch"
        assert pokemon.defense_iv == iv_spec["defense"], f"Pokemon {i}: defense IV mismatch"
        assert pokemon.speed_iv == iv_spec["speed"], f"Pokemon {i}: speed IV mismatch"
        assert pokemon.special_iv == iv_spec["special"], f"Pokemon {i}: special IV mismatch"
        
        # Test moves
        assert pokemon.moves == expected["moves"], f"Pokemon {i}: moves mismatch"
        
        # Test move names
        for move_id, expected_name in zip(pokemon.moves, expected["move_names"]):
            if expected_name:
                assert get_move_name(move_id) == expected_name


def test_collision_detection(save_state):
    """Test walkable matrix."""
    emu, spec = save_state
    expected = spec["collision"]
    
    walkable = emu.get_walkable_matrix()
    
    assert walkable.shape == (18, 20), "Matrix should be 18x20"
    
    if expected["has_walkable_tiles"]:
        assert walkable.sum() > 0, "Should have some walkable tiles"
    
    if expected["has_blocked_tiles"]:
        assert walkable.sum() < walkable.size, "Should have some blocked tiles"


def test_movement(save_state):
    """Test that movement updates position."""
    emu, spec = save_state
    
    # Get initial position
    _, x_before, y_before = read_player_position(emu)
    
    # Move down
    emu.press_button("down", frames=16)
    emu.tick(10)
    
    # Check position changed
    _, x_after, y_after = read_player_position(emu)
    
    assert y_after > y_before, "Y coordinate should increase when moving down"
    assert x_after == x_before, "X coordinate should not change"


def test_screenshot(save_state, tmp_path):
    """Test screenshot capture."""
    emu, _ = save_state
    
    screenshot_path = tmp_path / "test.png"
    emu.save_screenshot(str(screenshot_path))
    
    assert screenshot_path.exists(), "Screenshot file should be created"
    assert screenshot_path.stat().st_size > 0, "Screenshot should not be empty"
