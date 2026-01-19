"""Game state detection for Pokémon Red/Blue."""

from agentoak.emulator import GameBoyEmulator


def is_in_dialogue(emulator: GameBoyEmulator) -> bool:
    """Check if a text box/dialogue is currently displayed.
    
    Uses joypad polling flag - when disabled, usually means dialogue is active.
    """
    joypad_disabled = emulator.read_memory(0xFFF9, 1)[0]
    return joypad_disabled != 0


def can_advance_text(emulator: GameBoyEmulator) -> bool:
    """Check if we can press A to advance text.
    
    In Gen 1, text scrolls character by character. We need to wait
    until the full message is displayed before pressing A.
    
    For now, simple heuristic: wait a few frames after dialogue starts.
    """
    # TODO: Implement proper text completion detection
    # For now, assume we can always advance if in dialogue
    return is_in_dialogue(emulator)


def is_in_menu(emulator: GameBoyEmulator) -> bool:
    """Check if a menu is currently open.
    
    Menus have a cursor position at CC26.
    """
    cursor_pos = emulator.read_memory(0xCC26, 1)[0]
    # If cursor position is valid (0-255), likely in menu
    return cursor_pos != 0xFF


def get_menu_cursor_position(emulator: GameBoyEmulator) -> int:
    """Get current menu cursor position (0-indexed)."""
    return emulator.read_memory(0xCC26, 1)[0]


def is_in_battle(emulator: GameBoyEmulator) -> bool:
    """Check if currently in battle."""
    battle_flag = emulator.read_memory(0xD057, 1)[0]
    return battle_flag != 0


def is_at_title_screen(emulator: GameBoyEmulator) -> bool:
    """Check if at title screen by detecting white background + Pokémon logo.
    
    Title screen has:
    - White background (corners = 255)
    - Pokémon logo with dark pixels (0 or 153)
    
    This distinguishes it from:
    - Credits: white background but no logo (all 255)
    - Intro: black background (corners = 0)
    """
    screen = emulator.pyboy.screen.ndarray
    
    # Check corner (background color)
    corner = screen[0, 0, 0]
    
    # Check logo area (should have dark pixels at title screen)
    logo_top = screen[20, 80, 0]
    logo_mid = screen[30, 80, 0]
    
    # Title screen: white background + logo has dark pixels
    has_white_bg = corner == 255
    has_logo = logo_top < 255 or logo_mid < 255
    
    return has_white_bg and has_logo


def title_screen_has_version_text(emulator: GameBoyEmulator) -> bool:
    """Check if 'Version' text is visible and stable on title screen.
    
    We check row 52-56 where "XXX Version" appears.
    Text is considered stable when:
    1. There's text present (dark pixels)
    2. Left side has text (fully slid in)
    
    Note: This doesn't check frame-to-frame stability. That should be done
    by the caller by checking this function returns True for multiple frames.
    
    IMPORTANT: Only valid when is_at_title_screen() is True!
    """
    # First check if we're at title screen
    if not is_at_title_screen(emulator):
        return False
    
    screen = emulator.pyboy.screen.ndarray
    
    # Sample row 52 where "Blue/Red/Yellow Version" text appears
    # We focus on just this row to be more precise
    text_row = screen[52, 60:100, 0]
    
    # Check if there are dark pixels (text present)
    dark_pixels = (text_row < 150).sum()
    
    # Check if left part has text (means it's fully slid in)
    # Left 15 pixels should have text if it's arrived
    left_part = text_row[0:15]
    left_dark = (left_part < 150).sum()
    
    # Version text is visible when:
    # - Row has dark pixels > 15 (text is present)
    # - Left part has dark pixels > 5 (text has arrived on left)
    return dark_pixels > 15 and left_dark > 5


def is_menu_visible(emulator: GameBoyEmulator) -> bool:
    """Check if NEW GAME/OPTION menu is visible using OCR.
    
    Checks if the menu text region contains text.
    """
    from agentoak.ocr import screen_contains_text, REGION_MENU_TOP
    
    # Check if NEW GAME area has text
    return screen_contains_text(emulator, "NEW GAME", REGION_MENU_TOP)


def has_dialogue_arrow(emulator: GameBoyEmulator) -> bool:
    """Check if dialogue arrow (▼) is visible at bottom-right of text box.
    
    Arrow blinks (alternates between 0 and 255), so we check if the pixel
    is dark (0) which means arrow is currently visible.
    """
    screen = emulator.pyboy.screen.ndarray
    
    # Arrow position (bottom-right of text box)
    arrow_pixel = screen[130, 150, 0]
    
    # Arrow visible when pixel is dark (0)
    return arrow_pixel == 0


def wait_for_title_screen(emulator: GameBoyEmulator, max_frames: int = 1200) -> bool:
    """Wait until title screen is ready and stable, spamming A to skip intro faster.
    
    Args:
        emulator: Game emulator instance
        max_frames: Maximum frames to wait (default 20 seconds)
        
    Returns:
        True if title screen reached, False if timeout
    """
    stable_frames = 0
    
    for i in range(max_frames):
        if is_at_title_screen(emulator):
            stable_frames += 1
            # Wait for title screen to be stable for 30 frames (0.5 second)
            if stable_frames >= 30:
                return True
        else:
            stable_frames = 0
        
        # Spam A every 10 frames to skip intro faster
        if i % 10 == 0:
            emulator.press_button("a", frames=1)
        
        emulator.tick(1)
        
        # Log progress every 60 frames (1 second)
        if i % 60 == 0 and i > 0:
            print(f"      • Waiting... {i//60}s (stable: {stable_frames})")
    
    return False
