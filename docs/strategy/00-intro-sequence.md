# Intro Sequence - Pokémon Red/Blue

## TL;DR - Bot Action Sequence

```
1. Title screen → Press A
2. Select NEW GAME → Press A
3. Name selection → Select first preset → Press A
4. Rival name → Select first preset → Press A
5. Spawn in bedroom → Walk to PC → Press A
6. Select WITHDRAW ITEM → Select POTION → Press A (×2)
7. Walk to stairs → Go down
8. Walk to door → Exit house
9. Walk north toward grass → Oak auto-triggers
10. Oak leads to lab (automatic)
11. Walk to desired Poké Ball → Press A
12. Select YES → Press A
13. Nickname prompt → Select NO → Press A
14. Battle rival (use attack move, Potion if HP < 50%)
15. Exit lab → Head to Route 1
```

**Time:** ~3-4 minutes  
**Result:** Level 6 starter, 1 Potion, $175

---

## Overview

This document details the exact steps from starting a new game to obtaining your first Pokémon in Pokémon Red and Blue. Understanding this sequence is critical for the bot to properly initialize the game.

## Prerequisites

- ROM file loaded in PyBoy
- New game started (not continuing from save)

## Exact Sequence

### 1. Title Screen
1. Game displays intro cutscene with Gengar vs Nidorino
2. Title screen appears: "POKÉMON RED/BLUE VERSION"
3. Press **A** or **Start** to reach main menu

### 2. Main Menu
Options:
- **NEW GAME** - Start new adventure
- **OPTION** - Change settings (Text Speed, Battle Style, etc.)
- **CONTINUE** - Load existing save (not available on first boot)

**Action:** Select **NEW GAME** and press **A**

### 3. Professor Oak's Introduction
1. Professor Oak appears on screen
2. Oak's speech: "Hello there! Welcome to the world of POKéMON!"
3. Explains what Pokémon are
4. Shows a Nidorino as example
5. Introduces himself: "My name is OAK! People call me the POKéMON PROF!"

**Action:** Press **A** to advance through dialogue

### 4. Player Name Selection
Oak asks: "First, what is your name?"

**Options:**
- **Pokémon Red:** RED, ASH, JACK (preset names)
- **Pokémon Blue:** BLUE, GARY, JOHN (preset names)
- **NEW NAME** - Custom name (up to 7 characters)

**Recommendation for Bot:**
- Use preset name "RED" (in Red) or "BLUE" (in Blue)
- Faster than custom name entry
- No risk of input errors

**Action:** Select first preset name and press **A**

### 5. Rival Name Selection
Oak introduces his grandson: "This is my grandson. He's been your rival since you were a baby."

Oak asks: "...Erm, what is his name again?"

**Options:**
- **Pokémon Red:** BLUE, GARY, JOHN (preset names)
- **Pokémon Blue:** RED, ASH, JACK (preset names)
- **NEW NAME** - Custom name (up to 7 characters)

**Recommendation for Bot:**
- Use first preset name (BLUE in Red, RED in Blue)
- Consistent with speedrun strategies

**Action:** Select first preset name and press **A**

### 6. Spawn in Bedroom
Player spawns in their bedroom (2F of home in Pallet Town)

**Room contents:**
- Super Nintendo Entertainment System (can interact, does nothing)
- PC in corner (contains 1 Potion in storage)

**Action:** 
1. Walk to PC
2. Press **A** to interact
3. Select "WITHDRAW ITEM"
4. Select **POTION**
5. Potion added to Bag

### 7. Go Downstairs
**Action:** Walk to stairs (northeast corner) and press down

### 8. Talk to Mom (Optional)
Mom is sitting at table on 1F

Mom's dialogue: "OAK, next door, is looking for you."

**Action:** Walk to door mat (south wall) and exit house

### 9. Pallet Town - Oak Encounter Trigger
Player is now in Pallet Town

**Map layout:**
- West house: Player's home
- East house: Rival's home (sister Daisy inside)
- South building: Professor Oak's Laboratory
- North: Route 1 (tall grass visible)

**CRITICAL SEQUENCE:**
1. If player tries to walk north into Route 1 grass...
2. Professor Oak appears: "Hey! Wait! Don't go out!"
3. Oak: "It's unsafe! Wild POKéMON live in tall grass!"
4. Oak: "You need your own POKéMON for your protection. I know!"
5. Oak: "Here, come with me!"
6. Oak automatically leads player to his Laboratory

**Note:** This trigger is MANDATORY. You cannot skip it. Attempting to go anywhere else (Rival's house, south to water) does not progress the game.

### 10. Professor Oak's Laboratory
Oak leads you inside. Rival (Blue/Red) is already waiting.

Oak's dialogue: "These are POKéMON!"
Points to three Poké Balls on table.

Oak: "When I was young, I was a serious POKéMON trainer!"
Oak: "In my old age, I have only 3 left, but you can have one! Choose!"

### 11. Starter Selection
Three Poké Balls on table (left to right):
- **Left:** Bulbasaur
- **Middle:** Charmander  
- **Right:** Squirtle

**Action:** Walk to desired Poké Ball and press **A**

Confirmation prompt: "So! You want the [TYPE] POKéMON, [NAME]?"
- **YES** - Confirm selection
- **NO** - Cancel, choose again

After confirmation:
- Player receives starter Pokémon (Level 5)
- Pokémon added to party
- Nickname prompt appears: "Do you want to give a nickname to [NAME]?"
  - **Recommendation:** Select **NO** (faster, no input errors)

### 12. Rival's Selection
After player chooses, Rival speaks: "I'll take this one, then!"

**Rival's choice is ALWAYS type-advantaged against yours:**
- You pick Bulbasaur → Rival picks Charmander (Fire beats Grass)
- You pick Charmander → Rival picks Squirtle (Water beats Fire)
- You pick Squirtle → Rival picks Bulbasaur (Grass beats Water)

### 13. First Rival Battle
Rival immediately challenges you: "[RIVAL NAME] wants to fight!"

**Battle details:**
- Location: Professor Oak's Laboratory
- Rival's Pokémon: Level 5 (type advantage)
- Reward: $175 (Pokédollars)

**Moves available:**
- **Bulbasaur:** Tackle (Normal), Growl (Normal, lowers Attack)
- **Charmander:** Scratch (Normal), Growl (Normal, lowers Attack)
- **Squirtle:** Tackle (Normal), Tail Whip (Normal, lowers Defense)

**Strategy:**
- Use attacking move (Tackle/Scratch) repeatedly
- If HP drops below 50%, use Potion from Bag
- Rival will also use stat-lowering moves

**After victory:**
- Gain $175
- Starter reaches Level 6
- Rival leaves: "Okay! I'll make my POKéMON fight to toughen it up!"

### 14. Exit Laboratory
Oak: "To make a complete guide on all POKéMON in the world... That was my dream!"
Oak: "But, I'm too old! I can't do it!"
Oak: "So, I want you two to fulfill my dream for me!"
Oak: "Get out there and fill the POKéDEX!"

**Note:** You do NOT receive the Pokédex yet. That comes later after delivering Oak's Parcel from Viridian City.

**Action:** Exit laboratory, head north to Route 1

## Intro Sequence Complete

At this point:
- Player has starter Pokémon (Level 6)
- Has 1 Potion in Bag
- Has $175
- Can now proceed to Route 1

---

## Should You Let Oak Catch You?

**Answer: YES, it's MANDATORY.**

You CANNOT obtain a starter Pokémon without triggering Oak's encounter. The game is designed so that:
1. You cannot enter Route 1 without Oak stopping you
2. You cannot enter Rival's house (door is locked initially)
3. You cannot Surf south (no Pokémon, no HM)
4. Oak's Lab door is locked until Oak brings you there

**There is no way to skip or optimize this sequence.** The bot must follow it exactly.

---

## Are There Glitches in This Section?

**No useful glitches exist in the intro sequence.**

The only documented glitch is the "Introduction Nidorino Glitch" which is purely visual (Nidorino sprite corruption during Oak's intro speech) and has no gameplay impact.

All major glitches (Mew glitch, item duplication, etc.) require:
- Having a Pokémon with Fly
- Access to specific routes/trainers
- Items/HMs obtained later in game

**Conclusion:** The intro must be played normally. No shortcuts exist.

---

## Sources

- [Bulbapedia - Pokémon Red and Blue Walkthrough Part 1](https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Red_and_Blue/Part_1)
- [StrategyWiki - Pokémon Red and Blue Walkthrough](https://strategywiki.org/wiki/Pok%C3%A9mon_Red_and_Blue/Walkthrough)
- [Glitch City Wiki - Introduction Nidorino Glitch](https://glitchcity.wiki/wiki/Introduction_Nidorino_glitch)
