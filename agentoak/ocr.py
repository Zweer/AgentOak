"""Simple OCR for Game Boy text using template matching."""

import numpy as np
from agentoak.emulator import GameBoyEmulator


def extract_text_region(screen: np.ndarray, x: int, y: int, width: int, height: int) -> np.ndarray:
    """Extract a region from screen for text analysis.
    
    Args:
        screen: Screen array from PyBoy
        x, y: Top-left corner
        width, height: Region size
        
    Returns:
        Extracted region (grayscale, first channel only)
    """
    return screen[y:y+height, x:x+width, 0]


def region_has_text(region: np.ndarray, min_ratio: float = 0.05, max_ratio: float = 0.5) -> bool:
    """Check if a region contains text-like pixels.
    
    Args:
        region: Screen region to check
        min_ratio: Minimum ratio of dark pixels
        max_ratio: Maximum ratio of dark pixels
        
    Returns:
        True if region likely contains text
    """
    # Count dark pixels (text is black/dark on light background)
    dark_pixels = (region < 100).sum()
    total_pixels = region.size
    
    ratio = dark_pixels / total_pixels
    return min_ratio < ratio < max_ratio


def screen_contains_text(emulator: GameBoyEmulator, text: str, region: tuple = None) -> bool:
    """Check if screen contains specific text.
    
    Args:
        emulator: Game emulator instance
        text: Text to look for (e.g. "NEW GAME", "YES", "NO")
        region: Optional (x, y, width, height) to search in
        
    Returns:
        True if text likely present
    """
    screen = emulator.pyboy.screen.ndarray
    
    if region:
        x, y, w, h = region
        search_area = extract_text_region(screen, x, y, w, h)
    else:
        search_area = screen[:, :, 0]
    
    # Check if region has text
    return region_has_text(search_area)


# Common text regions (Game Boy screen is 160x144)
REGION_MENU_TOP = (8, 16, 48, 8)      # NEW GAME area
REGION_MENU_MID = (8, 24, 48, 8)      # OPTION/CONTINUE area
REGION_DIALOGUE = (8, 112, 144, 24)   # Bottom text box
REGION_YES_NO = (120, 70, 32, 24)     # YES/NO prompt area
