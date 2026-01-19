"""Intro sequence automation for Pokémon Red/Blue."""

from agentoak.emulator import GameBoyEmulator
from agentoak.game_state import (
    has_dialogue_arrow,
    is_at_title_screen,
    is_in_dialogue,
    is_in_menu,
    is_menu_visible,
    wait_for_title_screen,
)


def advance_dialogue(emulator: GameBoyEmulator, wait_frames: int = 30) -> None:
    """Advance through dialogue by pressing A when arrow appears.
    
    Args:
        emulator: Game emulator instance
        wait_frames: Max frames to wait for arrow (default 30 = 0.5s)
    """
    # Wait for dialogue arrow to appear
    for _ in range(wait_frames):
        if has_dialogue_arrow(emulator):
            break
        emulator.tick(1)
    
    # Press A to advance
    emulator.press_button("a", frames=1)
    emulator.tick(10)


def select_menu_option(emulator: GameBoyEmulator, option_index: int = 0) -> None:
    """Select a menu option by index.
    
    Args:
        emulator: Game emulator instance
        option_index: 0-indexed menu position (0 = first option)
    """
    # Move cursor to desired position
    for _ in range(option_index):
        emulator.press_button("down", frames=1)
        emulator.tick(5)
    
    # Confirm selection
    emulator.press_button("a", frames=1)
    emulator.tick(10)


def start_new_game(emulator: GameBoyEmulator) -> None:
    """Start a new game from title screen with precise timing.
    
    Sequence:
    1. A spam until title screen appears
    2. Wait for Version text
    3. Wait 120 frames after Version appears
    4. Press Start
    5. Wait for NEW GAME menu to be visible
    6. Press A to select NEW GAME
    """
    print("    → A spam until title screen appears...")
    
    # A spam until title screen
    for i in range(1200):  # 20 seconds max
        if is_at_title_screen(emulator):
            print(f"    → Title screen detected at frame {i}!")
            break
        if i % 10 == 0:
            emulator.press_button("a", frames=1)
        emulator.tick(1)
    
    # Wait for Version text to appear AND be stable
    print("    → Waiting for 'Version' text to be stable...")
    from agentoak.game_state import title_screen_has_version_text
    version_stable_frames = 0
    for i in range(300):  # 5 seconds max
        if title_screen_has_version_text(emulator):
            version_stable_frames += 1
            if version_stable_frames >= 60:  # Stable for 1 second
                print(f"    → 'Version' text stable for 60 frames!")
                emulator.save_screenshot("debug_version_detected.png")
                print("    → Screenshot saved: debug_version_detected.png")
                break
        else:
            version_stable_frames = 0
        emulator.tick(1)
    
    # Wait 60 more frames after stable
    print("    → Waiting 60 more frames for safety...")
    emulator.tick(60)
    
    print("    → Pressing Start...")
    emulator.press_button("start", frames=1)
    
    # Wait for NEW GAME menu
    print("    → Waiting for NEW GAME menu...")
    for i in range(300):  # 5 seconds max
        if is_menu_visible(emulator):
            print(f"    → NEW GAME menu visible at frame {i}!")
            emulator.save_screenshot("debug_menu_detected.png")
            print("    → Screenshot saved: debug_menu_detected.png")
            break
        emulator.tick(1)
    
    # Wait a bit before selecting
    print("    → Waiting 30 frames before selecting...")
    emulator.tick(30)
    
    print("    → Pressing A to select NEW GAME...")
    emulator.press_button("a", frames=1)
    emulator.tick(30)
    
    print("    ✓ New game started\n")


def skip_oak_intro(emulator: GameBoyEmulator) -> None:
    """Skip through Professor Oak's introduction dialogue.
    
    Oak's speech has multiple text boxes. We spam A to advance.
    """
    print("    → Advancing through dialogue...")
    # Oak's intro has ~10-12 dialogue boxes
    for i in range(15):
        if is_in_dialogue(emulator):
            print(f"      • Dialogue box {i+1}/15")
            advance_dialogue(emulator, wait_frames=20)
        else:
            emulator.tick(10)


def select_player_name(emulator: GameBoyEmulator, use_preset: bool = True) -> None:
    """Select player name.
    
    Args:
        emulator: Game emulator instance
        use_preset: If True, use first preset name (RED/BLUE)
    """
    print("    → At name selection screen...")
    if use_preset:
        print("    → Confirming preset name (RED/BLUE)...")
        # First preset is already selected, just confirm
        emulator.tick(30)
        emulator.press_button("a", frames=1)
        emulator.tick(30)
    else:
        # TODO: Implement custom name entry
        raise NotImplementedError("Custom name entry not yet implemented")


def select_rival_name(emulator: GameBoyEmulator, use_preset: bool = True) -> None:
    """Select rival name.
    
    Args:
        emulator: Game emulator instance
        use_preset: If True, use first preset name (BLUE/RED)
    """
    print("    → At rival name selection screen...")
    if use_preset:
        print("    → Confirming preset rival name (BLUE/RED)...")
        # First preset is already selected, just confirm
        emulator.tick(30)
        emulator.press_button("a", frames=1)
        emulator.tick(30)
    else:
        # TODO: Implement custom name entry
        raise NotImplementedError("Custom name entry not yet implemented")


def run_intro_sequence(
    emulator: GameBoyEmulator,
    starter: str = "bulbasaur",
    use_preset_names: bool = True,
) -> None:
    """Run the complete intro sequence.
    
    Args:
        emulator: Game emulator instance
        starter: Which starter to choose ("bulbasaur", "charmander", "squirtle")
        use_preset_names: Use preset names for player and rival
        
    Returns when player has starter and is ready to exit Oak's Lab.
    """
    print("\n🎮 Starting intro sequence...\n")
    
    # 1. Start new game
    print("📺 [1/10] Starting new game from title screen")
    start_new_game(emulator)
    print("    ✓ New game started\n")
    
    # 2. Skip Oak's intro
    print("👨‍🔬 [2/10] Professor Oak's introduction")
    skip_oak_intro(emulator)
    print("    ✓ Oak's intro complete\n")
    
    # 3. Select player name
    print("✏️  [3/10] Player name selection")
    select_player_name(emulator, use_preset=use_preset_names)
    skip_oak_intro(emulator)  # More dialogue after name
    print("    ✓ Player name selected\n")
    
    # 4. Select rival name
    print("✏️  [4/10] Rival name selection")
    select_rival_name(emulator, use_preset=use_preset_names)
    skip_oak_intro(emulator)  # More dialogue after rival name
    print("    ✓ Rival name selected\n")
    
    # 5. Spawn in bedroom - withdraw Potion from PC
    print("🏠 [5/10] Spawning in bedroom")
    print("    ⚠️  TODO: Withdraw Potion from PC")
    print("    ⚠️  TODO: Walk to stairs")
    print("    ⚠️  TODO: Go downstairs\n")
    
    # 6. Go downstairs and exit house
    print("🚪 [6/10] Exiting house")
    print("    ⚠️  TODO: Walk to door")
    print("    ⚠️  TODO: Exit to Pallet Town\n")
    
    # 7. Trigger Oak encounter
    print("🌿 [7/10] Triggering Oak encounter")
    print("    ⚠️  TODO: Walk north toward grass\n")
    
    # 8. Oak leads to lab (automatic)
    print("🏃 [8/10] Following Oak to lab")
    print("    → Waiting for Oak to lead us...")
    emulator.tick(300)  # Wait for Oak to lead us
    print("    ✓ Arrived at Oak's Lab\n")
    
    # 9. Choose starter
    print(f"⚡ [9/10] Choosing starter: {starter}")
    print("    ⚠️  TODO: Walk to Poké Ball")
    print("    ⚠️  TODO: Confirm selection")
    print("    ⚠️  TODO: Decline nickname\n")
    
    # 10. Battle rival
    print("⚔️  [10/10] First rival battle")
    print("    ⚠️  TODO: Battle logic")
    print("    ⚠️  TODO: Use attacks")
    print("    ⚠️  TODO: Use Potion if needed\n")
    
    print("✅ Intro sequence complete (partial implementation)!")
