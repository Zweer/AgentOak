"""Test memory reading with real save state."""

import json
from pathlib import Path

import numpy as np
import pytest

from agentoak.data import get_map_name, get_move_name, get_pokemon_name
from agentoak.emulator import GameBoyEmulator
from agentoak.memory import (
    is_pokemon_owned,
    read_badge_count,
    read_full_party,
    read_money,
    read_party_pokemon,
    read_play_time,
    read_player_name,
    read_player_position,
    read_pokedex_owned_count,
)


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


# Discover all save states dynamically
FIXTURES_DIR = Path(__file__).parent / "fixtures"
SAVE_STATES = [f.stem for f in FIXTURES_DIR.glob("*.state")]


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
    assert badges == expected


def test_player_name(save_state):
    """Test reading player name."""
    emu, spec = save_state
    expected = spec["player"]["name"]
    
    name = read_player_name(emu)
    assert name == expected


def test_money(save_state):
    """Test reading money."""
    emu, spec = save_state
    expected = spec["player"]["money"]
    
    money = read_money(emu)
    assert money == expected


def test_play_time(save_state):
    """Test reading play time."""
    emu, spec = save_state
    expected = spec["player"]["play_time"]
    
    time = read_play_time(emu)
    assert time["hours"] == expected["hours"]
    assert time["minutes"] == expected["minutes"]
    assert time["seconds"] == expected["seconds"]


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


def test_rom_not_found():
    """Test ROM file not found error."""
    with pytest.raises(FileNotFoundError):
        GameBoyEmulator("nonexistent.gb", headless=True)


def test_save_and_load_state(tmp_path):
    """Test save/load state."""
    emu = GameBoyEmulator("roms/pokemon-blue.gb", headless=True)
    save_path = Path(__file__).parent / "fixtures" / "bulbasaur.state"
    emu.load_state(str(save_path))
    emu.tick(60)
    
    # Save current state
    state_path = tmp_path / "test.state"
    emu.save_state(state_path)
    assert state_path.exists()
    
    # Read position before
    pos_before = read_player_position(emu)
    
    # Move and change state
    emu.press_button("down", frames=16)
    emu.tick(10)
    pos_after = read_player_position(emu)
    assert pos_after != pos_before
    
    # Load state back
    emu.load_state(state_path)
    emu.tick(10)
    pos_restored = read_player_position(emu)
    assert pos_restored == pos_before
    
    emu.close()


def test_empty_party_slot():
    """Test reading empty party slot."""
    emu = GameBoyEmulator("roms/pokemon-blue.gb", headless=True)
    save_path = Path(__file__).parent / "fixtures" / "bulbasaur.state"
    emu.load_state(str(save_path))
    emu.tick(60)
    
    # Slot 0 has Bulbasaur, slot 1 should be empty
    pokemon = read_party_pokemon(emu, 1)
    assert pokemon is None
    
    emu.close()


def test_pokedex_owned():
    """Test Pokédex owned check."""
    emu = GameBoyEmulator("roms/pokemon-blue.gb", headless=True)
    save_path = Path(__file__).parent / "fixtures" / "bulbasaur.state"
    emu.load_state(str(save_path))
    emu.tick(60)
    
    # Count owned
    count = read_pokedex_owned_count(emu)
    assert count >= 1  # At least Bulbasaur
    
    # Should have Bulbasaur (#1)
    assert is_pokemon_owned(emu, 1)
    
    # Should not have Mew (#151)
    assert not is_pokemon_owned(emu, 151)
    
    # Test invalid number
    with pytest.raises(ValueError):
        is_pokemon_owned(emu, 0)
    
    with pytest.raises(ValueError):
        is_pokemon_owned(emu, 152)
    
    emu.close()


def test_collision_without_wrapper():
    """Test collision detection fallback."""
    emu = GameBoyEmulator("roms/pokemon-blue.gb", headless=True)
    
    # Force game_wrapper to None
    emu.game_wrapper = None
    
    collision = emu.get_walkable_matrix()
    assert collision.shape == (18, 20)
    assert np.all(collision == 0)
    
    emu.close()
