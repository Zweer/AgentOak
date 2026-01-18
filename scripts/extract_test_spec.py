#!/usr/bin/env python3
"""Extract test specification from a save state."""

import json
import sys
from pathlib import Path

from agentoak.data import get_map_name, get_move_name, get_pokemon_name
from agentoak.emulator import GameBoyEmulator
from agentoak.memory import (
    read_badge_count,
    read_full_party,
    read_money,
    read_play_time,
    read_player_name,
    read_player_position,
)


def extract_spec(save_path: str, description: str = "") -> dict:
    """Extract test specification from save state."""
    print(f"Loading save state: {save_path}")
    
    emu = GameBoyEmulator("roms/pokemon-blue.gb", headless=True)
    emu.load_state(save_path)
    emu.tick(60)
    
    # Read player state
    name = read_player_name(emu)
    money = read_money(emu)
    time = read_play_time(emu)
    map_id, x, y = read_player_position(emu)
    badges = read_badge_count(emu)
    
    # Read party
    party = read_full_party(emu)
    party_data = []
    
    for pokemon in party:
        party_data.append({
            "species_id": pokemon.species_id,
            "name": get_pokemon_name(pokemon.species_id),
            "level": pokemon.level,
            "current_hp": pokemon.current_hp,
            "max_hp": pokemon.max_hp,
            "attack": pokemon.attack,
            "defense": pokemon.defense,
            "speed": pokemon.speed,
            "special": pokemon.special,
            "moves": pokemon.moves,
            "move_names": [
                get_move_name(m) if m != 0 else None
                for m in pokemon.moves
            ],
            "ivs": {
                "attack": pokemon.attack_iv,
                "defense": pokemon.defense_iv,
                "speed": pokemon.speed_iv,
                "special": pokemon.special_iv,
            }
        })
    
    # Check collision
    walkable = emu.get_walkable_matrix()
    has_walkable = bool(walkable.sum() > 0)
    has_blocked = bool(walkable.sum() < walkable.size)
    
    emu.close()
    
    # Build spec
    spec = {
        "description": description or f"Test save at {get_map_name(map_id)}",
        "player": {
            "name": name,
            "money": money,
            "play_time": time,
            "map_id": map_id,
            "map_name": get_map_name(map_id),
            "x": x,
            "y": y,
            "badges": badges,
        },
        "party": party_data,
        "pokedex": {
            "owned": len(party),  # Simplified for now
        },
        "collision": {
            "has_walkable_tiles": has_walkable,
            "has_blocked_tiles": has_blocked,
        }
    }
    
    return spec


def main():
    """Extract spec from save state."""
    if len(sys.argv) < 2:
        print("Usage: python extract_test_spec.py <save_state_path> [description]")
        print("\nExample:")
        print("  python extract_test_spec.py tests/fixtures/bulbasaur.state 'Starter Bulbasaur'")
        sys.exit(1)
    
    save_path = sys.argv[1]
    description = sys.argv[2] if len(sys.argv) > 2 else ""
    
    if not Path(save_path).exists():
        print(f"Error: Save state not found: {save_path}")
        sys.exit(1)
    
    # Extract spec
    spec = extract_spec(save_path, description)
    
    # Determine output path
    save_file = Path(save_path)
    json_path = save_file.with_suffix('.json')
    
    # Write JSON
    with open(json_path, 'w') as f:
        json.dump(spec, f, indent=2)
    
    print(f"\n✅ Spec written to: {json_path}")
    print(f"\nSummary:")
    print(f"  Location: {spec['player']['map_name']} ({spec['player']['x']}, {spec['player']['y']})")
    print(f"  Party: {len(spec['party'])} Pokémon")
    for i, p in enumerate(spec['party'], 1):
        print(f"    {i}. {p['name']} Lv.{p['level']}")
    print(f"  Badges: {spec['player']['badges']}")


if __name__ == "__main__":
    main()
