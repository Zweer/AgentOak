# Ideas from llm_pokemon_scaffold

Source: https://github.com/cicero225/llm_pokemon_scaffold

## Architecture Insights

### 1. Screenshot + Memory State
- Capture game screen as image
- Send to LLM with memory state
- LLM returns actions to execute

### 2. Meta-Critique System
- Periodic summary of game state
- Fact checking and organization
- Helps LLM stay on track
- Runs every N messages

### 3. Context Management
- Keep conversation history
- Summarize when context gets too long
- Maintain key facts across summaries

## What We Can Use

### For v1 (Full Version)
- [ ] Screenshot capture for LLM context
- [ ] Structured game state summary
- [ ] LLM integration for complex decisions
- [ ] Periodic state critique/validation

### Differences from Our Approach
- **Them**: LLM-driven (slow, expensive, exploratory)
- **Us**: Rule-based + LLM hybrid (fast, targeted, goal-oriented)

### Our Hybrid Strategy
1. **Rule-based** for:
   - Navigation (A* pathfinding)
   - Battle mechanics (type effectiveness)
   - Menu navigation
   - Catching logic

2. **LLM** for:
   - High-level planning (which Pokémon to catch next)
   - Complex decisions (trade-offs, priorities)
   - Error recovery (stuck situations)
   - Strategy adjustments

## Implementation Notes

- Use their prompt structure as reference
- Adapt their state representation
- Keep our rule-based core
- Add LLM as "advisor" layer

## References

- Original Anthropic starter: https://github.com/davidhershey/ClaudePlaysPokemonStarter
- Research article: https://www.lesswrong.com/posts/8aPyKyRrMAQatFSnG
