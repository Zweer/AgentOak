# AgentOak 🌳🤖

> "Professor Oak's dream, realized by AI"

An AI-powered agent that plays Pokémon Red/Blue to complete the Pokédex - all 151 Pokémon, including trades and glitches.

## Why AgentOak?

Professor Oak spent his life trying to complete the Pokédex. Now, with the power of AI and emulation, we can finally fulfill his dream - automatically.

AgentOak uses:
- **PyBoy** for Game Boy emulation with memory access
- **LLM integration** for intelligent decision-making
- **Dual-instance architecture** for trading between Red and Blue
- **Glitch execution** for Mew and item duplication

## Features

- 🎮 **Dual Game Support** - Runs Pokémon Blue and Red simultaneously
- 🔄 **Automated Trading** - Exchanges version-exclusive Pokémon
- 🧠 **Hybrid AI** - Rule-based logic + LLM for complex decisions
- 📊 **Live Dashboard** - Watch both games side-by-side with action logs
- 🐛 **Glitch Support** - Mew glitch, item duplication (MissingNo)
- 📈 **Progress Tracking** - Real-time Pokédex completion status

## Requirements

### System
- Python 3.11+
- ~500MB RAM per emulator instance

### Files (not included)
- `roms/pokemon-blue.gb` - Pokémon Blue ROM (SHA1: `d7037c83e1ae5b39bde3c30787637ba1d4c48ce2`)
- `roms/pokemon-red.gb` - Pokémon Red ROM (SHA1: `ea9bcae617fdf159b045185467ae58b2e4a48b9a`)

### Python Dependencies
```
pyboy>=2.0.0
numpy
pillow
pygame
```

## Installation

```bash
# Clone the repository
git clone https://github.com/Zweer/AgentOak.git
cd AgentOak

# Install with uv (recommended)
uv sync

# Or with pip
pip install -e .

# Add your ROMs
mkdir -p roms
# Copy pokemon-blue.gb and pokemon-red.gb to roms/
```

## Development

```bash
# Install dev dependencies
uv sync --extra dev

# Run tests
make test

# Run linter
make lint

# Format code
make format
```

### Creating Test Fixtures

Test fixtures are save states with corresponding JSON specifications for regression testing.

```bash
# 1. Play manually and create a save state
uv run python scripts/play_manual.py

# Press Ctrl+C when ready, choose 'y' for test mode
# This creates a .state file in tests/fixtures/

# 2. Extract test specification
uv run python scripts/extract_test_spec.py tests/fixtures/your_save.state "Description"

# This generates your_save.json with:
# - Player state (name, money, time, position, badges)
# - Party Pokémon (stats, moves, IVs)
# - Collision data

# 3. Tests run automatically for all .state files in tests/fixtures/
make test
```

## Usage

```bash
# Start the agent (both games)
python -m agentoak

# Start with display (watch the AI play)
python -m agentoak --display

# Dry run (no saves, just watch)
python -m agentoak --display --dry-run

# Start from existing save
python -m agentoak --load-state saves/checkpoint.state
```

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      ORCHESTRATOR                            │
│  - Tracks Pokédex progress                                  │
│  - Decides next objective                                   │
│  - Coordinates both game instances                          │
└─────────────────────┬───────────────────────────────────────┘
                      │
    ┌─────────────────┼─────────────────┐
    ▼                 ▼                 ▼
┌─────────┐    ┌───────────┐    ┌─────────────┐
│ Player  │    │  Glitch   │    │    Trade    │
│  Agent  │    │  Runner   │    │   Manager   │
└─────────┘    └───────────┘    └─────────────┘
    │                │                 │
    └────────────────┴─────────────────┘
                     │
             ┌───────┴───────┐
             ▼               ▼
       ┌──────────┐   ┌──────────┐
       │  PyBoy   │◄─►│  PyBoy   │
       │  (Blue)  │   │  (Red)   │
       └──────────┘   └──────────┘
```

## Roadmap

### v0 - Pilot (Current)
- [x] PyBoy integration (headless + display modes)
- [x] Memory reader (party, Pokédex, player state, money, time)
- [x] Input controller (button press with frame control)
- [x] Save/load state functionality
- [x] Screenshot capture
- [x] Collision detection (walkable matrix)
- [x] Test infrastructure with fixtures
- [x] 100% test coverage

### v1 - Full Pokédex Completion
- [ ] Map navigation (A* pathfinding)
- [ ] Battle system (attack, catch, run)
- [ ] Wild Pokémon encounters
- [ ] Badge collection
- [ ] HM usage (Cut, Surf, Strength, Flash)
- [ ] Key item management
- [ ] Catch all available Pokémon in one version
- [ ] Evolution handling (level, stones)
- [ ] Safari Zone strategy
- [ ] Mew glitch (Trainer-Fly)
- [ ] Item duplication (MissingNo) - optional
- [ ] Dual PyBoy instances
- [ ] Link cable emulation
- [ ] Trade protocol
- [ ] Version-exclusive exchanges
- [ ] Trade evolutions (Alakazam, Gengar, Machamp, Golem)
- [ ] Full 151 Pokémon
- [ ] Dashboard with live view
- [ ] Progress persistence

## Research Notes

### Glitch Compatibility
| Glitch | Red | Blue | Yellow |
|--------|-----|------|--------|
| Mew (Trainer-Fly) | ✅ | ✅ | ✅ |
| Item Duplication | ✅ | ✅ | ❌ |

### Version Exclusives
**Blue only:** Sandshrew, Sandslash, Vulpix, Ninetales, Meowth, Persian, Bellsprout, Weepinbell, Victreebel, Magmar, Pinsir

**Red only:** Ekans, Arbok, Oddish, Gloom, Vileplume, Mankey, Primeape, Growlithe, Arcanine, Scyther, Electabuzz

### Trade Evolutions
- Kadabra → Alakazam
- Machoke → Machamp
- Graveler → Golem
- Haunter → Gengar

## Contributing

This is an experimental/educational project. Contributions welcome!

## Credits & Acknowledgments

This project stands on the shoulders of giants:

- **[PyBoy](https://github.com/Baekalfen/PyBoy)** - The Game Boy emulator that makes this possible
- **[PokemonRedExperiments](https://github.com/PWhiddy/PokemonRedExperiments)** - RL approach to playing Pokémon Red
- **[llm_pokemon_scaffold](https://github.com/cicero225/llm_pokemon_scaffold)** - LLM-based Pokémon player
- **[Bulbapedia](https://bulbapedia.bulbagarden.net/)** - Pokémon data and memory maps
- **[pret/pokered](https://github.com/pret/pokered)** - Pokémon Red/Blue disassembly

## License

MIT

## Disclaimer

This project is for educational purposes. You must provide your own legally obtained ROM files. Pokémon is a trademark of Nintendo/Game Freak/The Pokémon Company.
