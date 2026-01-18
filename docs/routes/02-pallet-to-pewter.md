# 02: Pallet Town to Pewter City

## TL;DR - Bot Objectives

```
✓ Exit Oak's Lab → Route 1
✓ Reach Viridian City
✓ Get Oak's Parcel from Poké Mart
✓ Return to Pallet Town → deliver Parcel → get Pokédex
✓ Get Town Map from Daisy (Rival's sister)
✓ Buy Poké Balls in Viridian City
✓ (Optional) Battle Rival on Route 22
✓ Catch Pokémon on Route 2
✓ Navigate Viridian Forest
✓ Reach Pewter City
✓ Defeat Gym Leader Brock
```

**Time:** ~45-60 minutes  
**Pokédex Progress:** +6-8 species  
**Level Target:** 12-14 for Brock

---

## Overview

This is the first real chapter of the game. You'll get the Pokédex, catch your first wild Pokémon, and earn your first gym badge.

**Key Milestones:**
- Unlock Pokédex (required for tracking progress)
- Unlock Poké Balls (required for catching)
- First gym badge (Boulder Badge)
- Learn game mechanics (catching, battling trainers)

---

## Route: Pallet Town → Viridian City

### Starting Point
Exit Professor Oak's Laboratory after defeating Rival.

**Party Status:**
- Starter Pokémon (Level 6)
- 1 Potion in Bag
- $175

### Route 1 (North from Pallet)

**Wild Pokémon:**
| Pokémon | Level | Rate | Notes |
|---------|-------|------|-------|
| Pidgey | 2-5 | 50% | Normal/Flying, common |
| Rattata | 2-4 | 50% | Normal, common |

**Strategy:**
- **DO NOT try to catch Pokémon yet** (no Poké Balls)
- Battle wild Pokémon for EXP
- Avoid taking too much damage (save Potion for later)
- Goal: Reach Level 7-8 before Viridian City

**Free Sample:**
- Talk to man near signpost (south side of route)
- Receive free Potion
- **Bot action:** Walk to NPC, press A, receive Potion

### Viridian City (First Visit)

**City Layout:**
- Pokémon Center (west) - Heal here
- Poké Mart (northeast) - Get Oak's Parcel
- Pokémon Academy (center) - Optional tutorial
- Gym (north) - Locked (need 7 badges to enter)

**Critical Sequence:**

1. **Enter Poké Mart**
   - Shopkeeper recognizes you from Pallet Town
   - Automatically gives you Oak's Parcel
   - **Cannot buy items yet** (must deliver Parcel first)

2. **Hidden Item:**
   - Potion hidden near north exit (small tree)
   - **Bot action:** Check tile at coordinates (x, y) near Route 2 gate

3. **Pokémon Center:**
   - Heal your party (free)
   - Save game at PC
   - **Bot action:** Talk to nurse, select "Yes"

---

## Route: Viridian City → Pallet Town (Return Trip)

### Objective
Deliver Oak's Parcel to Professor Oak.

**Route 1 (South):**
- Same wild Pokémon as before
- Can use ledges (one-way jumps) to speed up return
- **Bot action:** Walk south, jump ledges when possible

### Pallet Town (Second Visit)

**Oak's Laboratory:**
1. Enter lab
2. Talk to Professor Oak
3. Deliver Oak's Parcel (custom Poké Ball)
4. Rival (Blue) arrives
5. Oak gives you **Pokédex**
6. Oak's request: "Fill the Pokédex with all Pokémon!"

**Pokédex Unlocked:**
- Now tracks all Pokémon seen and caught
- Essential for bot's progress tracking
- Updates automatically when encountering Pokémon

**Rival's House:**
1. Enter house east of yours
2. Talk to Daisy (Rival's sister)
3. Receive **Town Map**
4. Town Map shows current location and cities

**Bot Priority:**
- Pokédex is CRITICAL - must obtain before catching Pokémon
- Town Map is useful but not essential

---

## Route: Pallet Town → Viridian City (Second Trip)

### Objective
Stock up on supplies and prepare for Viridian Forest.

### Viridian City (Second Visit)

**Poké Mart - Now Open for Business:**

| Item | Price | Quantity to Buy |
|------|-------|-----------------|
| Poké Ball | $200 | 10-15 |
| Potion | $300 | 5 |
| Antidote | $100 | 3-5 |

**Budget:**
- Current money: $175 (from Rival battle)
- Need: ~$2500 for recommended supplies
- **Problem:** Not enough money!

**Solution: Grind on Route 1/22**
- Battle wild Pokémon for money
- Each battle gives ~$5-10
- Need ~20-30 battles to afford supplies
- **Alternative:** Buy fewer Poké Balls initially (5-7), catch Pokémon, sell items if needed

**Recommended Purchase (Budget):**
- 5 Poké Balls ($1000)
- 3 Potions ($900)
- 2 Antidotes ($200)
- **Total:** $2100

**Old Man Tutorial:**
- Old man north of Pokémon Center (was blocking path before)
- Asks: "Are you in a hurry?"
- If you say "No," he demonstrates catching Pokémon
- **Bot action:** Say "Yes" to skip tutorial (faster)

---

## Route 22 (Optional Detour)

### Should You Go Here?

**Pros:**
- Catch new Pokémon (Nidoran♂/♀, Spearow)
- Extra EXP from wild battles
- Rival battle gives $280 (helps with Poké Ball budget)

**Cons:**
- Rival battle is harder than first fight
- Risk of fainting (lose money, return to Pokémon Center)
- Takes extra time (~10 minutes)

**Recommendation for Bot:**
- **YES, do this detour** if you need money for Poké Balls
- **NO, skip it** if you already have enough money

### Wild Pokémon (Route 22)

| Pokémon | Level | Rate | Version | Notes |
|---------|-------|------|---------|-------|
| Rattata | 2-4 | 45% | Both | Common |
| Spearow | 3, 5 | 10% | Both | Flying-type, useful later |
| Nidoran♀ | 2-4 | 40% | Blue / 5% Red | Poison-type |
| Nidoran♂ | 2-4 | 40% Red / 5% Blue | Poison-type |

**Catching Priority:**
1. **Nidoran♂ or ♀** (whichever is common in your version) - Evolves into strong Pokémon
2. **Spearow** - Flying-type, learns Fly later

### Rival Battle #2 (Optional)

**Location:** Partway into Route 22

**Rival's Team:**
- Pidgey (Lv9) - Normal/Flying, knows Gust and Sand-Attack
- Starter counter (Lv8) - Type advantage against your starter

**Strategy:**

**If you have Bulbasaur (vs Charmander):**
- Use Vine Whip (learned at Lv13) if you have it
- Otherwise use Tackle
- Charmander is weak, should be easy
- Watch out for Pidgey's Gust

**If you have Charmander (vs Squirtle):**
- **HARD BATTLE** - Squirtle has Bubble (Water-type)
- Use Scratch on Pidgey first (easier target)
- Save Potions for Squirtle fight
- May need to overlevel to Lv10-11

**If you have Squirtle (vs Bulbasaur):**
- Use Tackle (Bubble not effective against Grass)
- Bulbasaur has Leech Seed (drains HP each turn)
- Kill quickly before Leech Seed stacks
- Moderate difficulty

**Reward:** $280 (helps buy Poké Balls!)

**Bot Decision Logic:**
```
if money < 1000:
    go to Route 22
    battle Rival
    catch Nidoran
    return to Viridian
else:
    skip Route 22
    proceed to Route 2
```

---

## Route 2 (West Side)

### Overview
Route 2 connects Viridian City to Pewter City. The east side is blocked by Cut trees (can't access yet). The west side leads through Viridian Forest.

### Wild Pokémon (Route 2 - Before Forest)

| Pokémon | Level | Rate | Version | Notes |
|---------|-------|------|---------|-------|
| Pidgey | 3-5 | 45% | Both | Common |
| Rattata | 2-5 | 40% | Both | Common |
| Caterpie | 3-5 | 15% | Red | Bug-type, evolves fast |
| Weedle | 3-5 | 15% | Blue | Bug-type, evolves fast |

**Catching Priority:**
1. **Caterpie (Red) or Weedle (Blue)** - Evolves quickly, useful for early game
   - Caterpie → Metapod (Lv7) → Butterfree (Lv10)
   - Weedle → Kakuna (Lv7) → Beedrill (Lv10)

**Strategy:**
- Catch 1-2 Pokémon here before entering forest
- Save most Poké Balls for Viridian Forest (better Pokémon)
- Heal at Viridian City if HP is low

---

## Viridian Forest

### Overview
Large forest maze filled with Bug Catchers (trainers) and Bug-type Pokémon. First real dungeon.

**Layout:**
- Multiple paths (some lead to dead ends)
- Trainers cannot be avoided (will spot you)
- Items scattered throughout
- Exit leads to Route 2 (north side) → Pewter City

### Wild Pokémon (Viridian Forest)

| Pokémon | Level | Rate | Version | Notes |
|---------|-------|------|---------|-------|
| Caterpie | 3-5 | 50% | Red | Bug-type |
| Weedle | 3-5 | 50% | Blue | Bug-type |
| Metapod | 3-6 | 30% | Red | Caterpie evolution |
| Kakuna | 3-6 | 30% | Blue | Weedle evolution |
| Pikachu | 3-5 | 5% | Both | **RARE** - Electric-type, iconic |

**Catching Priority:**
1. **Pikachu** (5% encounter rate) - Rare, useful Electric-type
   - Keep walking in grass until you find one
   - Use Poké Balls liberally (worth it)
   - Pikachu is strong early game, learns Thunderbolt later

2. **Caterpie/Weedle** (if you didn't catch on Route 2)
   - Fast evolution = quick Pokédex entries
   - Butterfree learns Confusion (Psychic-type move, strong)

### Items in Viridian Forest

| Item | Location | Notes |
|------|----------|-------|
| Poké Ball | Near entrance | Free Poké Ball |
| Potion | Middle area | Heal item |
| Antidote | Left path after 2nd Bug Catcher | Cures Poison |

**Bot Strategy:**
- Collect all items (marked on map)
- Antidote is important (Bug Pokémon inflict Poison)

### Trainers in Viridian Forest

**Bug Catcher #1:**
- Weedle (Lv6) / Caterpie (Lv6)
- Reward: $60

**Bug Catcher #2:**
- Weedle (Lv7), Kakuna (Lv7), Weedle (Lv7) / Caterpie (Lv7), Metapod (Lv7), Caterpie (Lv7)
- Reward: $70

**Bug Catcher #3:**
- Weedle (Lv9) / Caterpie (Lv9)
- Reward: $90

**Total Earnings:** $220

**Strategy:**
- Bug-type Pokémon are weak
- Use Tackle/Scratch to defeat quickly
- Watch out for Poison Sting (Weedle) - inflicts Poison status
- Use Antidote if poisoned (or heal at Pokémon Center after forest)

### Navigation Tips

**Optimal Path (for bot):**
1. Enter forest from south gate
2. Go north, collect Poké Ball
3. Battle Bug Catcher #1
4. Go east, then north
5. Battle Bug Catcher #2
6. Go west, collect Antidote
7. Go north, collect Potion
8. Battle Bug Catcher #3
9. Exit north to Route 2

**Time in Forest:** ~15-20 minutes

**Level After Forest:** Should be Lv10-12

---

## Route 2 (North Side)

### Overview
Short path from Viridian Forest exit to Pewter City.

**Wild Pokémon:** Same as south side (Pidgey, Rattata, Caterpie/Weedle)

**Strategy:**
- Heal if needed (Pewter City has Pokémon Center)
- Don't catch more Pokémon here (already have them)
- Proceed directly to Pewter City

---

## Pewter City

### Overview
Small city known for its museum and Rock-type Gym. First gym challenge.

**City Layout:**
- Pokémon Center (south)
- Poké Mart (northeast)
- Museum (north) - Costs $50 to enter (optional)
- Gym (west) - Brock, Rock-type specialist

### Poké Mart (Pewter City)

**New Items Available:**
| Item | Price | Notes |
|------|-------|-------|
| Poké Ball | $200 | Stock up if low |
| Potion | $300 | Buy 5-10 |
| Escape Rope | $550 | Escape dungeons (not needed yet) |
| Antidote | $100 | Cure Poison |
| Burn Heal | $250 | Cure Burn |
| Awakening | $200 | Cure Sleep |
| Parlyz Heal | $200 | Cure Paralysis |

**Recommended Purchases:**
- 5 Potions ($1500) - For gym battle
- 5 Poké Balls ($1000) - Restock
- 2 Antidotes ($200) - Just in case

**Current Money:** ~$175 (start) + $280 (Rival) + $220 (Bug Catchers) = $675
- **Not enough!** Need to grind more or skip some purchases

### Museum (Optional)

**Cost:** $50 entry fee

**Inside:**
- Old Amber (hidden item, needed for Aerodactyl later)
- Scientist gives you Old Amber if you talk to him
- Various exhibits (flavor text)

**Bot Decision:**
- **YES, enter museum** - Old Amber is required for Pokédex completion
- Aerodactyl (#142) can only be obtained by reviving Old Amber at Cinnabar Island

**How to Get Old Amber:**
1. Pay $50 at entrance
2. Go upstairs
3. Talk to scientist in front of Aerodactyl exhibit
4. Receive Old Amber
5. Store in Bag (Key Items)

### Preparing for Brock

**Level Check:**
- Bulbasaur: Lv12+ (learns Vine Whip at Lv13 - CRITICAL)
- Charmander: Lv14+ (will still struggle)
- Squirtle: Lv12+ (learns Bubble at Lv8, should be fine)

**If Bulbasaur and below Lv13:**
- **MUST grind to Lv13** for Vine Whip
- Vine Whip is super effective against Rock-type
- Without it, battle is much harder

**If Charmander:**
- **VERY HARD BATTLE** - Fire is weak to Rock
- Recommended: Catch Mankey on Route 22 (learns Low Kick, Fighting-type)
- Or catch Nidoran and level it up (learns Double Kick at Lv12)
- Or overlevel to Lv16+ and brute force with Ember

**Grinding Spots:**
- Route 2 (north or south)
- Viridian Forest (if you want more Bug Pokémon)
- Route 22 (Nidoran, Spearow)

---

## Pewter Gym - Gym Leader Brock

### Gym Layout
- 2 trainers before Brock (optional, can skip by walking around)
- Brock at the back

**Jr. Trainer (optional):**
- Diglett (Lv11), Sandshrew (Lv11)
- Reward: $220
- **Bot decision:** Skip to save time (can walk around)

**Jr. Trainer (optional):**
- Geodude (Lv10), Geodude (Lv10), Geodude (Lv10)
- Reward: $200
- **Bot decision:** Skip to save time

### Gym Leader Brock

**Badge:** Boulder Badge (1/8)  
**Reward:** $1386 + TM34 (Bide)  
**Effect:** Pokémon up to Lv20 obey you, can use Flash outside battle

**Brock's Team:**

**Geodude (Lv12)**
- Type: Rock/Ground
- Moves: Tackle, Defense Curl
- Weak to: Water, Grass, Fighting, Ground, Steel, Ice
- Strategy: Easy to defeat with Bulbasaur/Squirtle

**Onix (Lv14)**
- Type: Rock/Ground  
- Moves: Tackle, Screech, Bide, Bind
- Weak to: Water, Grass, Fighting, Ground, Steel, Ice
- **High Defense** but low HP
- Strategy: Use super effective moves

### Battle Strategy by Starter

**Bulbasaur (EASY):**
```
Turn 1: Vine Whip on Geodude (1-2 hit KO)
Turn 2: Vine Whip on Onix (2-3 hit KO)
Victory in ~3-4 turns
```
- Vine Whip is 2x super effective (Grass vs Rock/Ground)
- Should take minimal damage
- No Potions needed

**Squirtle (MODERATE):**
```
Turn 1: Bubble on Geodude (2-3 hit KO)
Turn 2-3: Bubble on Onix (3-4 hit KO)
Victory in ~5-6 turns
```
- Bubble is 2x super effective (Water vs Rock/Ground)
- Onix may use Bide (stores damage, returns 2x next turn)
- Use Potion if HP drops below 50%

**Charmander (HARD):**
```
Option 1: Use Mankey with Low Kick
- Low Kick is super effective (Fighting vs Rock)
- Mankey should be Lv12+

Option 2: Use Nidoran with Double Kick
- Double Kick is super effective (Fighting vs Rock)
- Nidoran should be Lv12+

Option 3: Brute force with Charmander
- Ember is NOT VERY EFFECTIVE
- Need to be Lv16+ to survive
- Use multiple Potions
```

**Recommended for Charmander users:**
- Catch Mankey on Route 22 (5% in Red, 40% in Blue)
- Level to Lv12 (learns Low Kick at Lv9)
- Use Mankey as main attacker
- Keep Charmander as backup

### After Defeating Brock

**Rewards:**
- Boulder Badge (1/8)
- $1386 (good money!)
- TM34 (Bide) - Not very useful, can skip teaching it

**Badge Effects:**
- Pokémon up to Lv20 obey you (even traded ones)
- Can use Flash HM outside battle (get Flash later)
- Attack stat slightly increased for all Pokémon

**Next Steps:**
- Heal at Pokémon Center
- Save game
- Exit Pewter City east to Route 3

---

## Pokédex Progress Check

**By end of this chapter, you should have:**

**Seen:** 10-15 species  
**Caught:** 6-10 species

**Recommended catches:**
1. Starter (Bulbasaur/Charmander/Squirtle)
2. Pidgey (Route 1)
3. Rattata (Route 1)
4. Nidoran♂ or ♀ (Route 22)
5. Caterpie or Weedle (Route 2 / Viridian Forest)
6. Metapod or Kakuna (Viridian Forest)
7. Pikachu (Viridian Forest - if found)
8. Spearow (Route 22 - optional)

**Evolution opportunities:**
- Caterpie → Metapod (Lv7) → Butterfree (Lv10)
- Weedle → Kakuna (Lv7) → Beedrill (Lv10)
- Nidoran♂ → Nidorino (Lv16)
- Nidoran♀ → Nidorina (Lv16)

---

## Bot Implementation Notes

### Critical Path
```
1. Route 1 → Viridian City
2. Get Oak's Parcel
3. Return to Pallet Town
4. Deliver Parcel → Get Pokédex
5. Get Town Map from Daisy
6. Return to Viridian City
7. Buy Poké Balls
8. (Optional) Route 22 → Rival battle
9. Route 2 → Viridian Forest
10. Catch Pikachu in forest (5% rate, may take time)
11. Exit forest → Pewter City
12. Enter Museum → Get Old Amber
13. Grind to Lv13 (Bulbasaur) or Lv12 (Squirtle)
14. Challenge Brock
15. Defeat Brock → Get Boulder Badge
```

### Decision Points

**Money Management:**
- If money < $1000: Grind on Route 1/22 until $1000+
- If money >= $1000: Buy Poké Balls and proceed

**Pikachu Hunting:**
- 5% encounter rate = ~20 encounters average
- Set max attempts: 50 encounters
- If not found after 50, proceed (can catch later)

**Brock Battle:**
- If Bulbasaur < Lv13: Grind until Lv13 (Vine Whip)
- If Charmander: Catch Mankey/Nidoran first, level to Lv12
- If Squirtle >= Lv12: Proceed to battle

### Error Handling

**If party faints:**
- Respawn at last Pokémon Center
- Lose 50% of money
- Heal and retry

**If out of Poké Balls:**
- Return to Viridian/Pewter Poké Mart
- Buy more (need money from trainer battles)

**If out of Potions during Brock:**
- Flee from battle (lose money)
- Buy more Potions
- Retry battle

---

## Summary

**Objectives Completed:**
✅ Obtained Pokédex  
✅ Obtained Town Map  
✅ Caught 6-10 Pokémon  
✅ Defeated Gym Leader Brock  
✅ Earned Boulder Badge (1/8)  
✅ Obtained Old Amber (for Aerodactyl)

**Party Level:** 12-14  
**Money:** ~$1500-2000  
**Pokédex:** 6-10 caught, 10-15 seen

**Next Chapter:** [03: Pewter City to Cerulean City](03-pewter-to-cerulean.md)
- Route 3 (many trainers)
- Mt. Moon (first real dungeon, fossils!)
- Route 4
- Cerulean City
- Gym Leader Misty (Water-type)

---

## Sources

- [Bulbapedia - Pokémon Red and Blue Walkthrough Part 2](https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Red_and_Blue/Part_2)
- [Bulbapedia - Viridian Forest](https://bulbapedia.bulbagarden.net/wiki/Viridian_Forest)
- [Bulbapedia - Pewter Gym](https://bulbapedia.bulbagarden.net/wiki/Pewter_Gym)
- [StrategyWiki - Pokémon Red and Blue Walkthrough](https://strategywiki.org/wiki/Pok%C3%A9mon_Red_and_Blue/Walkthrough)

**Content was rephrased for compliance with licensing restrictions**
