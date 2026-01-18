# AgentOak v0 - Pilot Requirements

> Minimal viable prototype to validate the approach

## Goal

Create a working foundation that proves we can:
1. Run PyBoy and control it programmatically
2. Read game state from memory
3. Send inputs and see results
4. Display the game screen

**NOT in scope for v0**: Full gameplay, trading, glitches, AI decision-making.

## Requirements

### R1: PyBoy Integration

#### R1.1: Emulator Setup
- [ ] Load Pokémon Blue ROM
- [ ] Run in headless mode (no window)
- [ ] Run in display mode (SDL2 window)
- [ ] Advance frames programmatically

#### R1.2: Input Control
- [ ] Send button presses (A, B, Start, Select, D-pad)
- [ ] Release buttons
- [ ] Hold buttons for multiple frames

#### R1.3: State Management
- [ ] Save state to file
- [ ] Load state from file

### R2: Memory Reader

#### R2.1: Party Pokémon
- [ ] Read party count (0-6)
- [ ] Read species ID for each party member
- [ ] Read level for each party member
- [ ] Read current HP for each party member

#### R2.2: Pokédex
- [ ] Read owned Pokémon bitfield
- [ ] Count total owned
- [ ] Check if specific Pokémon is owned

#### R2.3: Player State
- [ ] Read current map ID
- [ ] Read X/Y coordinates
- [ ] Read badge count

### R3: Basic Display

#### R3.1: Screen Capture
- [ ] Get screen as numpy array
- [ ] Convert to PIL Image
- [ ] Save screenshot to file

#### R3.2: Simple Viewer (optional for v0)
- [ ] Display game screen in window
- [ ] Update at ~15 FPS
- [ ] Show basic stats overlay (party count, badges)

### R4: Proof of Concept

#### R4.1: Demo Script
- [ ] Load game from title screen
- [ ] Navigate to a specific location (e.g., walk out of house)
- [ ] Print game state to console
- [ ] Save screenshot

## Technical Specifications

### Memory Addresses (Red/Blue English)

```python
# Party
PARTY_COUNT = 0xD163        # 1 byte: number of Pokémon in party
PARTY_SPECIES_LIST = 0xD164 # 6 bytes: species IDs (terminated by 0xFF)
PARTY_POKEMON_1 = 0xD16B    # 44 bytes: first Pokémon data

# Pokémon data structure (44 bytes each)
# Offset 0x00: Species ID (1 byte)
# Offset 0x01: Current HP (2 bytes, big-endian)
# Offset 0x03: Level (1 byte) - box level, recalculated on withdraw
# Offset 0x21: Level (1 byte) - actual level
# ... (see Bulbapedia for full structure)

# Pokédex
POKEDEX_OWNED = 0xD2F7      # 19 bytes: bitfield of owned Pokémon
POKEDEX_SEEN = 0xD30A       # 19 bytes: bitfield of seen Pokémon

# Player
MAP_ID = 0xD35E             # 1 byte: current map
PLAYER_Y = 0xD361           # 1 byte: Y coordinate
PLAYER_X = 0xD362           # 1 byte: X coordinate
BADGES = 0xD356             # 1 byte: badge bitfield
```

### Pokédex Bitfield

The Pokédex uses a bitfield where each bit represents one Pokémon:
- Byte 0, bit 0 = Pokémon #1 (Bulbasaur)
- Byte 0, bit 7 = Pokémon #8 (Wartortle)
- Byte 18, bit 6 = Pokémon #151 (Mew)

```python
def is_pokemon_owned(memory: bytes, pokedex_num: int) -> bool:
    """Check if a Pokémon is owned (1-indexed)."""
    byte_index = (pokedex_num - 1) // 8
    bit_index = (pokedex_num - 1) % 8
    return bool(memory[POKEDEX_OWNED + byte_index] & (1 << bit_index))
```

### Project Structure (v0)

```
AgentOak/
├── agentoak/
│   ├── __init__.py
│   ├── __main__.py      # Entry point
│   ├── emulator.py      # PyBoy wrapper
│   └── memory/
│       ├── __init__.py
│       ├── reader.py    # Memory reading functions
│       └── addresses.py # Constants
├── scripts/
│   └── demo.py          # Proof of concept demo
├── roms/                # User provides ROMs (gitignored)
├── saves/               # Save states
├── requirements.txt
└── README.md
```

### Dependencies

```
# requirements.txt
pyboy>=2.0.0
numpy>=1.24.0
pillow>=10.0.0
```

## Success Criteria

v0 is complete when:

1. ✅ `python -m agentoak` starts the emulator
2. ✅ Can read party Pokémon from memory
3. ✅ Can read Pokédex owned count
4. ✅ Can send inputs (walk around)
5. ✅ Can save/load state
6. ✅ Demo script runs successfully

## Out of Scope

These are explicitly NOT part of v0:
- Navigation/pathfinding
- Battle system
- Catching Pokémon
- Menu interaction
- Trading
- Glitches
- Dashboard UI
- LLM integration
- Second game instance (Red)

## Timeline

Estimated: 1-2 days for a working v0.
