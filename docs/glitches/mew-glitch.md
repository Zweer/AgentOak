# Mew Glitch (Trainer-Fly Glitch)

## Overview

The Mew glitch, also known as the Trainer-Fly glitch, is a method to encounter and catch Mew in Pokémon Red, Blue, and Yellow. This is the **only legitimate way** to obtain Mew in these games without external events or cheating devices.

**Compatibility:**
- ✅ Pokémon Red
- ✅ Pokémon Blue  
- ✅ Pokémon Yellow

**Difficulty:** Medium (requires precise timing)  
**Risk:** Low (can retry if failed)  
**Result:** Mew at Level 7

---

## Prerequisites

### Required Items
- ✅ HM02 (Fly) - Obtained from Route 16 house
- ✅ A Pokémon that knows Fly
- ✅ Access to Route 8 (between Lavender Town and Saffron City)
- ✅ Access to Route 24/25 (north of Cerulean City)

### Required Trainers (MUST NOT BE DEFEATED YET)
1. **Gambler on Route 8** (facing north, near Underground Path entrance)
   - Location: Route 8, east of Saffron City gate
   - Team: Poliwag (Lv22), Poliwag (Lv22), Poliwhirl (Lv22)
   - **CRITICAL:** Must not have battled this trainer yet!

2. **Youngster on Route 25** (has Slowpoke)
   - Location: Route 25, east path after Nugget Bridge
   - Team: Slowpoke (Lv17), other Pokémon
   - **CRITICAL:** Must not have battled this trainer yet!

### Why These Specific Trainers?

**Gambler on Route 8:**
- Has long line of sight (can see you from off-screen)
- Allows you to trigger battle and Fly away before he reaches you

**Youngster with Slowpoke:**
- Slowpoke has Special stat of 21
- Special stat 21 corresponds to Mew's index number
- This is what makes Mew appear!

---

## Step-by-Step Instructions

### Phase 1: Setup (Route 8)

1. **Save your game** before starting
   - Location: Route 8, in front of Underground Path door
   - This allows you to retry if you mess up

2. **Position yourself correctly**
   - Stand directly in front of Underground Path entrance (Route 8 side)
   - Face south (toward Lavender Town)
   - Gambler should be off-screen to your right

3. **Walk down ONE step**
   - Press Down on D-pad
   - **IMMEDIATELY press Start** during the step
   - Timing is critical!

4. **If successful:**
   - Start menu opens
   - Gambler's "!" appears above his head
   - He starts walking toward you
   - But you're in the menu, so he can't reach you yet

5. **If failed:**
   - Gambler reaches you and battle starts
   - Reset game and try again
   - Practice the timing: Down + Start simultaneously

6. **Open Pokémon menu**
   - Select Pokémon that knows Fly
   - Use Fly
   - Fly to **Cerulean City**

7. **What happens:**
   - Gambler "sees" you just as you fly away
   - Game registers battle as "pending"
   - Start button stops working (this is normal!)

### Phase 2: Trigger Battle (Route 25)

8. **Walk to Route 24**
   - Exit Cerulean City north
   - Cross Nugget Bridge

9. **Go to Route 25**
   - Continue east from Nugget Bridge
   - Find the Youngster with Slowpoke
   - **He must walk to you** (don't talk to him directly)

10. **Battle the Youngster**
    - Let him see you and walk to you
    - Battle starts normally
    - Defeat his Slowpoke (and other Pokémon)
    - Battle ends

11. **After battle:**
    - Start button works again!
    - Game has "cleared" the pending battle flag

### Phase 3: Encounter Mew (Route 8)

12. **Fly to Lavender Town**
    - Use Fly
    - Go to Lavender Town

13. **Walk west to Route 8**
    - Exit Lavender Town west
    - Enter Route 8

14. **Menu pops up automatically!**
    - As soon as you enter Route 8
    - Start menu appears by itself
    - Press B to close it

15. **Mew appears!**
    - Wild Mew (Level 7)
    - Battle starts

### Phase 4: Catch Mew

16. **Battle Strategy:**
    - Mew is Level 7 (very weak)
    - Don't attack! (might faint it)
    - Use status moves: Sleep, Paralyze
    - Throw Ultra Balls or Great Balls

17. **Recommended approach:**
    - Turn 1: Use Sleep Powder / Hypnosis / Spore
    - Turn 2+: Throw Poké Balls until caught

18. **Mew's Stats (Level 7):**
    - HP: ~25
    - Moves: Pound
    - Very easy to catch when asleep

19. **Success!**
    - Mew is caught
    - Pokédex entry #151 registered
    - Congratulations!

---

## Troubleshooting

### "I pressed Start too late, Gambler battled me"
- Reset game and try again
- Practice timing: Press Start DURING the step, not after

### "Start button still doesn't work after Youngster battle"
- Make sure Youngster walked to you (don't talk to him)
- Try battling a different trainer on Route 24/25

### "Menu didn't pop up on Route 8"
- Make sure you battled the Youngster with Slowpoke
- Make sure you flew to Lavender Town (not walked)
- Try exiting and re-entering Route 8

### "I already defeated the Gambler on Route 8"
- You can use other trainers with long line of sight
- Alternative: Youngster on Route 24 (before Nugget Bridge)
- Same process, different location

### "I already defeated the Youngster with Slowpoke"
- You can use other trainers with different Special stats
- Different Special stats = different Pokémon
- Special 21 = Mew, but you can get other Pokémon too

---

## Alternative Trainers

### For Phase 1 (Long Line of Sight):
- **Jr. Trainer♂ on Route 24** (before Nugget Bridge)
- **Jr. Trainer♂ on Route 6** (south of Vermilion)
- Any trainer that can see you from off-screen

### For Phase 2 (Special Stat 21):
- **Youngster with Slowpoke on Route 25** (recommended)
- Any Pokémon with Special stat 21

### Other Pokémon You Can Get:
By battling trainers with different Special stats, you can encounter different Pokémon:
- Special 7 = Jynx
- Special 15 = Mew (alternative method)
- Special 21 = Mew (standard method)
- Special 183 = Mewtwo (but causes glitches)

---

## Technical Explanation

**Why does this work?**

1. When you Fly away from Gambler, game sets "battle pending" flag
2. This disables Start button and some other functions
3. When you battle Youngster, game clears the flag
4. But game also stores Youngster's last Pokémon's Special stat
5. When you return to Route 8, game tries to resume "pending" battle
6. Game uses stored Special stat as Pokémon index number
7. Special 21 = Mew's index number
8. Mew appears!

**Is this safe?**
- Yes! This is a harmless glitch
- Won't corrupt your save file
- Can be done multiple times
- Mew is legitimate and can be traded

---

## Bot Implementation Notes

### Critical Checks Before Starting:
```python
def can_do_mew_glitch():
    checks = {
        "has_fly": player.has_hm(HM.FLY),
        "pokemon_knows_fly": any(p.knows_move("Fly") for p in party),
        "gambler_not_defeated": not trainer_defeated("Route8_Gambler"),
        "youngster_not_defeated": not trainer_defeated("Route25_Youngster_Slowpoke"),
        "can_access_route8": player.can_reach("Route8"),
        "can_access_route25": player.can_reach("Route25")
    }
    return all(checks.values())
```

### Timing for Start Button:
```python
def trigger_trainer_fly():
    # Position in front of Underground Path
    move_to_position(route8_underground_entrance)
    
    # Walk down and press Start simultaneously
    # Frame-perfect timing required
    press_down()
    wait_frames(1)  # Wait 1 frame
    press_start()   # Press Start on same frame as step completes
    
    # Check if menu opened
    if menu_is_open():
        # Success! Fly away
        select_pokemon_with_fly()
        use_fly("Cerulean City")
        return True
    else:
        # Failed, reset and retry
        reset_game()
        return False
```

### Verification:
```python
def verify_mew_encounter():
    # After returning to Route 8
    if menu_opens_automatically():
        close_menu()
        if wild_pokemon_appears():
            if pokemon_is_mew():
                return True
    return False
```

---

## Summary Checklist

- [ ] Have Fly HM and Pokémon that knows Fly
- [ ] Gambler on Route 8 not defeated
- [ ] Youngster with Slowpoke on Route 25 not defeated
- [ ] Save game before starting
- [ ] Position in front of Underground Path (Route 8)
- [ ] Walk down + Press Start (frame-perfect)
- [ ] Fly to Cerulean City
- [ ] Battle Youngster on Route 25 (let him walk to you)
- [ ] Fly to Lavender Town
- [ ] Walk west to Route 8
- [ ] Menu pops up automatically
- [ ] Mew appears at Level 7
- [ ] Catch Mew with Poké Balls

---

## Sources

- [Bulbapedia - Mew Glitch](https://bulbapedia.bulbagarden.net/wiki/Mew_glitch)
- [Glitch City Wiki - Trainer-Fly Glitch](https://glitchcity.wiki/wiki/Trainer-Fly_glitch)
- Community testing and verification

**Content was rephrased for compliance with licensing restrictions**
