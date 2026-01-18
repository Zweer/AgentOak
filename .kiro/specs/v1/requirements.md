# AgentOak v1 - Full Requirements

> Complete the Pokédex: All 151 Pokémon

## Goal

An autonomous agent that plays Pokémon Blue and Red to catch all 151 Pokémon, including:
- All catchable Pokémon in both versions
- Version exclusives (via trading)
- Trade evolutions (Alakazam, Gengar, Machamp, Golem)
- Mew (via glitch)

## Requirements

### R1: Core Systems

#### R1.1: Dual Emulator Support
- [ ] Run two PyBoy instances simultaneously (Blue + Red)
- [ ] Independent game loops
- [ ] Synchronized for trading
- [ ] Separate save states

#### R1.2: Memory Reader (Enhanced)
- [ ] Full party data (all 44 bytes per Pokémon)
- [ ] PC box Pokémon
- [ ] Inventory (items, quantities)
- [ ] Money
- [ ] Game progress flags
- [ ] Battle state (in battle, wild/trainer, enemy HP)

#### R1.3: Input System
- [ ] Reliable button press/release
- [ ] Input sequences (macros)
- [ ] Frame-perfect inputs for glitches
- [ ] Menu navigation helpers

### R2: Navigation

#### R2.1: Map System
- [ ] Load map data (walkable tiles, warps)
- [ ] Track current location
- [ ] Detect map transitions

#### R2.2: Pathfinding
- [ ] A* algorithm for navigation
- [ ] Handle obstacles (NPCs, ledges)
- [ ] Multi-map routing
- [ ] HM obstacle handling (Cut trees, Surf water, Strength boulders)

#### R2.3: Movement
- [ ] Walk to coordinates
- [ ] Use Fly to fast travel
- [ ] Enter/exit buildings
- [ ] Navigate caves (Flash support)

### R3: Battle System

#### R3.1: Battle Detection
- [ ] Detect battle start
- [ ] Identify wild vs trainer battle
- [ ] Read enemy Pokémon data

#### R3.2: Battle Actions
- [ ] Select moves
- [ ] Use items (Poké Balls, potions)
- [ ] Switch Pokémon
- [ ] Run from battle

#### R3.3: Catching
- [ ] Calculate catch probability
- [ ] Select appropriate ball
- [ ] Weaken Pokémon first (if needed)
- [ ] Handle catch success/failure

#### R3.4: Battle Strategy
- [ ] Type effectiveness awareness
- [ ] HP management
- [ ] PP management
- [ ] Healing when needed

### R4: Story Progression

#### R4.1: Badge Collection
- [ ] Navigate to each gym
- [ ] Defeat gym leaders
- [ ] Track badge progress

#### R4.2: Key Events
- [ ] Get starter Pokémon
- [ ] Obtain Pokédex
- [ ] Get HMs (Cut, Fly, Surf, Strength, Flash)
- [ ] Wake Snorlax (Poké Flute)
- [ ] Defeat Elite Four (for some evolutions/areas)

#### R4.3: Item Management
- [ ] Buy Poké Balls
- [ ] Manage inventory space
- [ ] Use evolution stones
- [ ] Key items (Silph Scope, etc.)

### R5: Pokémon Collection

#### R5.1: Wild Encounters
- [ ] Know where each Pokémon spawns
- [ ] Encounter rate awareness
- [ ] Safari Zone handling
- [ ] Fishing (Old Rod, Good Rod, Super Rod)

#### R5.2: Gift Pokémon
- [ ] Starter selection
- [ ] Eevee (Celadon)
- [ ] Lapras (Silph Co.)
- [ ] Fossils (Helix/Dome → Omanyte/Kabuto)
- [ ] Magikarp (Mt. Moon)
- [ ] Hitmonlee/Hitmonchan (Fighting Dojo)

#### R5.3: Evolutions
- [ ] Level-up evolutions
- [ ] Stone evolutions (buy/find stones)
- [ ] Trade evolutions (coordinate with other instance)

#### R5.4: Legendary Pokémon
- [ ] Articuno (Seafoam Islands)
- [ ] Zapdos (Power Plant)
- [ ] Moltres (Victory Road)
- [ ] Mewtwo (Cerulean Cave - post-game)

### R6: Glitch Execution

#### R6.1: Mew Glitch (Trainer-Fly)
- [ ] Prerequisites check (Fly, specific trainers undefeated)
- [ ] Execute Trainer-Fly sequence
- [ ] Trigger Mew encounter (Special stat manipulation)
- [ ] Catch Mew

#### R6.2: Item Duplication (Optional)
- [ ] MissingNo encounter setup
- [ ] Duplicate Master Balls
- [ ] Duplicate Rare Candies
- [ ] Note: Only works in Red/Blue, not Yellow

### R7: Trading System

#### R7.1: Link Cable Emulation
- [ ] Connect two PyBoy instances
- [ ] Establish link connection
- [ ] Handle trade protocol

#### R7.2: Trade Execution
- [ ] Enter Cable Club
- [ ] Select Pokémon to trade
- [ ] Confirm trade
- [ ] Verify trade completion

#### R7.3: Trade Planning
- [ ] List version exclusives needed
- [ ] Plan trade order
- [ ] Handle trade evolutions (trade back)

### R8: Dashboard

#### R8.1: Dual Display
- [ ] Show both game screens side-by-side
- [ ] 15-30 FPS refresh rate
- [ ] Resizable window

#### R8.2: Status Panel
- [ ] Current objective for each game
- [ ] Party summary
- [ ] Pokédex progress (X/151)
- [ ] Badges collected

#### R8.3: Action Log
- [ ] Timestamped events
- [ ] Color-coded by game (Blue/Red)
- [ ] Scrollable history
- [ ] Filter by event type

#### R8.4: Controls
- [ ] Pause/Resume
- [ ] Speed control (1x, 2x, 4x)
- [ ] Manual save
- [ ] Screenshot

### R9: Orchestrator

#### R9.1: Objective Planning
- [ ] Determine next Pokémon to catch
- [ ] Prioritize by accessibility
- [ ] Handle dependencies (need Surf to reach X)

#### R9.2: Multi-Game Coordination
- [ ] Assign tasks to Blue/Red
- [ ] Synchronize for trades
- [ ] Balance progress between games

#### R9.3: Progress Tracking
- [ ] Persistent state (survives restart)
- [ ] Pokédex checklist
- [ ] Completed objectives log

### R10: LLM Integration (Optional Enhancement)

#### R10.1: Decision Support
- [ ] Complex navigation decisions
- [ ] Battle strategy suggestions
- [ ] Error recovery

#### R10.2: Logging
- [ ] Explain current action
- [ ] Summarize progress
- [ ] Debug assistance

## Data Requirements

### Pokémon Data
```json
{
  "pokemon": [
    {
      "id": 1,
      "name": "Bulbasaur",
      "type1": "Grass",
      "type2": "Poison",
      "locations": {
        "blue": ["Cerulean City (gift)"],
        "red": ["Cerulean City (gift)"]
      },
      "evolution": {
        "method": "level",
        "level": 16,
        "into": 2
      }
    }
  ]
}
```

### Version Exclusives
```json
{
  "blue_only": [27, 28, 37, 38, 52, 53, 69, 70, 71, 126, 127],
  "red_only": [23, 24, 43, 44, 45, 56, 57, 58, 59, 123, 125]
}
```

### Trade Evolutions
```json
{
  "trade_evolutions": [
    {"from": 64, "to": 65, "name": "Kadabra → Alakazam"},
    {"from": 67, "to": 68, "name": "Machoke → Machamp"},
    {"from": 75, "to": 76, "name": "Graveler → Golem"},
    {"from": 93, "to": 94, "name": "Haunter → Gengar"}
  ]
}
```

## Success Criteria

v1 is complete when:

1. ✅ Agent can complete the game (8 badges, Elite Four)
2. ✅ Agent catches all non-exclusive Pokémon in one version
3. ✅ Agent executes Mew glitch successfully
4. ✅ Trading between Blue and Red works
5. ✅ All 151 Pokémon registered in Pokédex
6. ✅ Dashboard shows live progress
7. ✅ Can run unattended for hours

## Milestones

### M1: Single Game Completion
- Complete story (8 badges)
- Catch all available Pokémon in Blue
- ~80-100 Pokémon

### M2: Glitch Mastery
- Execute Mew glitch
- (Optional) Item duplication
- +1 Pokémon (Mew)

### M3: Trading Infrastructure
- Dual instance running
- Link cable working
- Basic trade execution

### M4: Full Pokédex
- Trade all exclusives
- Trade evolutions
- 151/151 complete

### M5: Polish
- Dashboard complete
- Robust error handling
- Documentation

## Timeline

Estimated: 4-6 weeks for full v1.

## Documentation Requirements

Before implementation, detailed strategy documents must be created in `docs/`:

### docs/strategy/
| Document | Content |
|----------|---------|
| `starter-selection.md` | Which starter for Blue vs Red, why |
| `fossil-strategy.md` | Helix vs Dome per version, timing |
| `game-corner.md` | Coin farming, which Pokémon to buy (Porygon, Dratini, etc.) |
| `safari-zone.md` | Optimal route, bait/rock strategy, target Pokémon |
| `in-game-trades.md` | All NPC trades, what to prepare |
| `legendary-pokemon.md` | Catch strategy for birds + Mewtwo |
| `missable-pokemon.md` | One-time-only Pokémon, when to get them |

### docs/glitches/
| Document | Content |
|----------|---------|
| `mew-glitch.md` | Exact Trainer-Fly sequence, prerequisites, timing |
| `item-duplication.md` | MissingNo setup, which items to duplicate |

### docs/routes/
| Document | Content |
|----------|---------|
| `optimal-route.md` | Full playthrough order for Pokédex completion |
| `badge-order.md` | Gym order and requirements |
| `hm-progression.md` | When each HM is needed and obtained |

### docs/data/
| Document | Content |
|----------|---------|
| `pokemon-locations.json` | All 151 Pokémon with catch locations |
| `version-exclusives.json` | Blue-only and Red-only lists |
| `evolution-requirements.json` | Level, stone, trade requirements |
| `map-connections.json` | Map IDs and how they connect |
| `memory-addresses.json` | All RAM addresses used |

These documents will be created incrementally as we research and implement each feature.

## Research Notes

### Missable Pokémon
Some Pokémon can only be obtained once per save:
- Starter (Bulbasaur/Charmander/Squirtle)
- Eevee
- Fossils (Helix OR Dome, not both)
- Hitmonlee OR Hitmonchan
- Snorlax (2 total, but limited)
- Legendary birds (1 each)
- Mewtwo (1)

### Safari Zone Strategy
- 500 steps limit
- No weakening Pokémon
- Bait/Rock mechanics
- Target rare Pokémon: Chansey, Kangaskhan, Tauros, Scyther/Pinsir

### Optimal Route (TBD)
Need to research:
- Speedrun routes for reference
- Pokédex completion guides
- Minimum badges needed for each area
