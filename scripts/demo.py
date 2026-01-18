#!/usr/bin/env python3
"""Demo script to test PyBoy integration and memory reading."""

from agentoak.emulator import GameBoyEmulator
from agentoak.memory import (
    read_badge_count,
    read_party_count,
    read_player_position,
    read_pokedex_owned_count,
)


def main():
    print("🎮 AgentOak v0 - PyBoy Integration Test\n")
    
    # Load Pokémon Blue
    print("Loading Pokémon Blue...")
    emu = GameBoyEmulator("roms/pokemon-blue.gb", headless=True)
    
    # Skip intro (press Start a few times)
    print("Skipping intro...")
    for _ in range(10):
        emu.tick(60)  # Wait 1 second (60 frames)
        emu.press_button("start", frames=10)
    
    # Read game state
    print("\n📊 Game State:")
    print(f"  Party count: {read_party_count(emu)}")
    print(f"  Pokédex owned: {read_pokedex_owned_count(emu)}")
    print(f"  Badges: {read_badge_count(emu)}")
    
    map_id, x, y = read_player_position(emu)
    print(f"  Position: Map {map_id}, ({x}, {y})")
    
    # Test GameWrapper collision detection
    print("\n🗺️  Testing collision detection...")
    walkable = emu.get_walkable_matrix()
    print(f"  Walkable matrix shape: {walkable.shape}")
    print(f"  Walkable tiles: {walkable.sum()}/{walkable.size}")
    
    # Test save state
    print("\n💾 Testing save state...")
    emu.save_state("saves/test.state")
    print("  ✓ State saved to saves/test.state")
    
    emu.close()
    print("\n✅ Test complete!")


if __name__ == "__main__":
    main()
