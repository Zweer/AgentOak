# Game Corner Strategy

## Overview

The Celadon Game Corner is a casino where you can win coins and exchange them for rare Pokémon and TMs. Some Pokémon are ONLY available here (Porygon!).

**Location:** Celadon City (southeast)  
**Cost:** $1000 = 50 coins  
**Prizes:** Pokémon, TMs

---

## How It Works

### Buying Coins

**Coin Counter (inside Game Corner):**
- 50 coins = $1000
- Can buy as many as you want (if you have money)

### Playing Slot Machines

**Slot Machine Mechanics:**
- Insert coins (1-3 coins per spin)
- Pull lever
- Match 3 symbols to win
- Payouts: 15, 100, or 300 coins

**Win Rates:**
- Very low (designed to lose money)
- Average: Lose 60-70% of coins
- **NOT RECOMMENDED for bot!**

### Finding Free Coins

**Hidden Coins on Floor:**
- Check floor tiles in Game Corner
- Some tiles have hidden coins
- Total: ~20-30 coins can be found

**Talking to NPCs:**
- Some NPCs give hints about coins
- One NPC gives you coins

---

## Prize Corner

**Location:** Next door to Game Corner

### Pokémon Prizes

| Pokémon | Coins | Version | Notes |
|---------|-------|---------|-------|
| **Porygon** | 9999 | Both | **ONLY WAY TO GET PORYGON!** |
| **Dratini** | 2800 | Red | Dragon-type, evolves to Dragonite |
| **Dratini** | 4600 | Blue | Dragon-type (more expensive in Blue) |
| **Scyther** | 5500 | Red | Bug/Flying, version exclusive |
| **Pinsir** | 2500 | Blue | Bug, version exclusive |
| Abra | 180 | Both | Psychic-type (available elsewhere) |
| Clefairy | 500 | Both | Normal-type (available elsewhere) |
| Nidorina | 1200 | Red | Poison-type (available elsewhere) |
| Nidorino | 1200 | Blue | Poison-type (available elsewhere) |

### TM Prizes

| TM | Move | Type | Power | Coins |
|----|------|------|-------|-------|
| TM23 | Dragon Rage | Dragon | 40 (fixed) | 3300 |
| TM15 | Hyper Beam | Normal | 150 | 5500 |
| TM50 | Substitute | Normal | - | 7700 |

---

## Priority Pokémon

### 1. Porygon (9999 coins) - CRITICAL!

**Why:**
- **ONLY way to get Porygon in Gen 1!**
- Can't catch in wild
- Can't get from NPCs
- Can't evolve from anything
- **MUST buy from Game Corner**

**Cost:**
- 9999 coins
- = $199,980 (if buying all coins)
- Very expensive!

**Strategy:**
- Save up money from trainers
- Use item duplication glitch for Nuggets
- Sell Nuggets for money
- Buy coins
- Get Porygon

### 2. Dratini (2800/4600 coins) - HIGH PRIORITY

**Why:**
- Dragon-type (rare!)
- Evolves to Dragonite (Lv55)
- Dragonite is pseudo-legendary (very strong)
- Can catch in Safari Zone, but very rare (1% in one specific area)

**Cost:**
- Red: 2800 coins = $56,000
- Blue: 4600 coins = $92,000

**Strategy:**
- Easier to buy than catch in Safari Zone
- Get after Porygon

### 3. Scyther (Red) / Pinsir (Blue) - MEDIUM PRIORITY

**Why:**
- Version exclusive
- Can catch in Safari Zone (4-5% rate)
- But buying is guaranteed

**Cost:**
- Scyther (Red): 5500 coins = $110,000
- Pinsir (Blue): 2500 coins = $50,000

**Strategy:**
- Try to catch in Safari Zone first
- If can't find after 3-4 runs, buy from Game Corner

---

## Coin Farming Strategies

### Strategy 1: Buy Coins (RECOMMENDED)

**Pros:**
- ✅ Fast
- ✅ Guaranteed
- ✅ No RNG

**Cons:**
- ❌ Expensive

**How:**
1. Farm money from trainers
2. Use item duplication glitch (Nugget ×255)
3. Sell Nuggets ($5000 each)
4. Buy coins ($1000 = 50 coins)
5. Repeat until you have enough

**Time:** ~5 minutes per 1000 coins  
**Cost:** $20,000 per 1000 coins

### Strategy 2: Play Slot Machines (NOT RECOMMENDED)

**Pros:**
- ✅ Can win big (rarely)

**Cons:**
- ❌ Very slow
- ❌ Lose money on average
- ❌ RNG-dependent
- ❌ Boring

**How:**
1. Insert 3 coins
2. Pull lever
3. Hope for 3 matching symbols
4. Repeat 1000+ times

**Time:** ~2-3 hours per 1000 coins  
**Expected Loss:** 60-70% of coins

**Bot should NOT use this strategy!**

### Strategy 3: Find Free Coins

**Pros:**
- ✅ Free!

**Cons:**
- ❌ Only ~20-30 coins total
- ❌ Not enough for anything

**How:**
1. Walk around Game Corner
2. Press A on every floor tile
3. Some tiles have hidden coins
4. Collect all

**Total:** ~20-30 coins (not enough for anything useful)

---

## Optimal Coin Spending Order

### For Pokédex Completion:

**Priority 1: Porygon (9999 coins)**
- MUST HAVE
- Only way to get it
- Get first

**Priority 2: Dratini (2800/4600 coins)**
- Dragon-type
- Evolves to Dragonite
- Get second

**Priority 3: Scyther (Red) / Pinsir (Blue) (5500/2500 coins)**
- Version exclusive
- Try Safari Zone first
- Buy if can't find

**Priority 4: TM15 Hyper Beam (5500 coins)**
- Strongest Normal-type move
- Optional, but useful

**Total Coins Needed:**
- Red: 9999 + 2800 + 5500 = 18,299 coins
- Blue: 9999 + 4600 + 2500 = 17,099 coins

**Total Cost:**
- Red: ~$365,980
- Blue: ~$341,980

---

## Money Farming for Game Corner

### Method 1: Item Duplication Glitch

**Best Method!**

1. Do MissingNo glitch
2. Duplicate Nuggets (×255)
3. Sell Nuggets ($5000 each)
4. Total: $1,275,000
5. Buy all coins needed

**Time:** ~10 minutes  
**Result:** Unlimited money

### Method 2: Trainer Battles

**Slow but legitimate**

1. Battle all trainers in game
2. Elite Four gives most money
3. Rematch Elite Four multiple times

**Time:** ~2-3 hours  
**Result:** ~$100,000-200,000

### Method 3: Selling Items

**Moderate method**

Items to sell:
- Nugget: $5000
- Big Pearl: $3750
- Pearl: $700
- Stardust: $1000
- Star Piece: $4900

**Time:** Depends on items found  
**Result:** Variable

---

## Bot Implementation

### Coin Acquisition Strategy

```python
def get_game_corner_pokemon():
    # Step 1: Farm money
    if not has_enough_money():
        farm_money_via_missingno()  # Duplicate Nuggets
    
    # Step 2: Buy coins
    total_coins_needed = calculate_coins_needed()
    buy_coins(total_coins_needed)
    
    # Step 3: Buy Pokemon in priority order
    buy_pokemon("Porygon", 9999)
    buy_pokemon("Dratini", 2800 if version == "Red" else 4600)
    
    if not caught_in_safari_zone("Scyther" if version == "Red" else "Pinsir"):
        buy_pokemon("Scyther" if version == "Red" else "Pinsir", 
                   5500 if version == "Red" else 2500)
```

### Money Farming

```python
def farm_money_via_missingno():
    # Use item duplication glitch
    prepare_item_for_duplication("Nugget")
    execute_missingno_glitch()
    
    # Now have 255 Nuggets
    sell_items("Nugget", quantity=200)  # Keep some for later
    
    # Result: $1,000,000+
    return get_current_money()
```

### Coin Purchase

```python
def buy_coins(amount_needed):
    coins_per_purchase = 50
    cost_per_purchase = 1000
    
    purchases_needed = math.ceil(amount_needed / coins_per_purchase)
    total_cost = purchases_needed * cost_per_purchase
    
    if get_current_money() < total_cost:
        raise InsufficientFundsError()
    
    for _ in range(purchases_needed):
        talk_to_coin_clerk()
        select_option("Buy 50 coins")
        confirm_purchase()
    
    return get_current_coins()
```

### Prize Redemption

```python
def buy_pokemon_from_prize_corner(pokemon_name, coin_cost):
    if get_current_coins() < coin_cost:
        raise InsufficientCoinsError()
    
    enter_prize_corner()
    talk_to_clerk()
    select_pokemon(pokemon_name)
    confirm_purchase()
    
    # Pokemon added to party or PC
    return verify_pokemon_obtained(pokemon_name)
```

---

## Time Estimates

### With Item Duplication Glitch:

**Total Time:** ~30 minutes
- MissingNo glitch: 5 minutes
- Sell Nuggets: 5 minutes
- Buy coins: 10 minutes
- Buy Pokémon: 5 minutes
- Verify: 5 minutes

### Without Glitch:

**Total Time:** ~5-10 hours
- Farm money: 3-5 hours
- Buy coins: 1-2 hours
- Buy Pokémon: 5 minutes
- Verify: 5 minutes

**Recommendation: Use item duplication glitch!**

---

## Common Mistakes

### ❌ Playing Slot Machines
- Waste of time
- Lose money on average
- Bot should NEVER do this

### ❌ Buying Low-Priority Pokémon First
- Abra, Clefairy, Nidorina/Nidorino available elsewhere
- Don't waste coins on them
- Focus on Porygon, Dratini, Scyther/Pinsir

### ❌ Not Using Item Duplication
- Farming money legitimately takes hours
- Item duplication takes 10 minutes
- Use the glitch!

### ❌ Forgetting About Porygon
- Porygon is ONLY available here
- Don't skip it!
- Get it first

---

## Summary Checklist

- [ ] Farm money (item duplication glitch recommended)
- [ ] Go to Celadon Game Corner
- [ ] Buy coins (50 coins = $1000)
- [ ] Go to Prize Corner (next door)
- [ ] Buy Porygon (9999 coins) - CRITICAL!
- [ ] Buy Dratini (2800/4600 coins)
- [ ] Buy Scyther (Red) / Pinsir (Blue) if not caught in Safari Zone
- [ ] Optional: Buy TM15 Hyper Beam (5500 coins)
- [ ] Verify all Pokémon obtained

**Total Cost:** ~$340,000-370,000  
**Total Time:** ~30 minutes (with glitch)

---

## Sources

- [Bulbapedia - Celadon Game Corner](https://bulbapedia.bulbagarden.net/wiki/Celadon_Game_Corner)
- [Bulbapedia - Prize Corner](https://bulbapedia.bulbagarden.net/wiki/Celadon_Prize_Corner)
- Community strategies

**Content was rephrased for compliance with licensing restrictions**
