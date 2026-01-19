#!/usr/bin/env python3
"""Debug intro sequence with detailed state tracking."""

import signal
import sys

from agentoak.emulator import GameBoyEmulator
from agentoak.game_state import is_at_title_screen, title_screen_has_version_text

ROM_PATH = "roms/pokemon-blue.gb"

emu = None


def signal_handler(sig, frame):
    print("\n\n🛑 Interrupted")
    if emu:
        emu.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

emu = GameBoyEmulator(ROM_PATH, headless=False)

print("🎮 Monitoring intro sequence with detailed state")
print("A spam every 10 frames to skip intro\n")
print("States tracked:")
print("  - Title: Logo visible (white bg + dark logo)")
print("  - Version: 'Version' text visible below logo")
print("  - White: Center screen is mostly white (settled)\n")

frame = 0
title_stable = 0
version_stable = 0
title_appeared = False  # Track when title first appears
prev_text_region = None  # Track previous frame's text region

try:
    while frame < 3600:  # 60 seconds max
        # Check states
        at_title = is_at_title_screen(emu)
        
        # Check if center is white (settled)
        screen = emu.pyboy.screen.ndarray
        center_region = screen[60:80, 60:100, 0]
        white_pixels = (center_region > 200).sum()
        total_pixels = center_region.size
        white_ratio = white_pixels / total_pixels
        is_white = white_ratio > 0.9
        
        # Check Version text stability manually
        text_region = screen[48:54, 60:100, 0]
        dark_pixels = (text_region < 150).sum()
        left_part = screen[48:54, 60:70, 0]
        left_dark = (left_part < 150).sum()
        
        # Check if region is stable (same as previous frame)
        is_stable = False
        if prev_text_region is not None:
            diff = abs(text_region.astype(int) - prev_text_region.astype(int)).sum()
            is_stable = diff < 10  # Very small difference = stable
        prev_text_region = text_region.copy()
        
        # Version is visible when: has text + left part filled + stable
        has_version = (dark_pixels > 25 and left_dark > 5 and is_stable)
        
        # Track when title first appears
        if at_title and not title_appeared:
            title_appeared = True
            print(f"\n    🎯 Title screen appeared at frame {frame}! Stopping A spam.\n")
        
        # Track stability
        if at_title:
            title_stable += 1
        else:
            title_stable = 0
            
        if has_version:
            version_stable += 1
        else:
            version_stable = 0
        
        # Print every 6 frames (10 times per second)
        if frame % 6 == 0:
            title_icon = "✅" if at_title else "❌"
            version_icon = "✅" if has_version else "❌"
            white_icon = "✅" if is_white else "❌"
            stable_icon = "✅" if is_stable else "❌"
            
            print(f"[{frame//60:2d}s {frame%60:02d}f] "
                  f"Title:{title_icon}({title_stable:3d}) | "
                  f"Version:{version_icon}({version_stable:3d}) | "
                  f"Stable:{stable_icon} Dark:{dark_pixels:2d} Left:{left_dark:2d} | "
                  f"White:{white_icon}({white_ratio:.2f})")
        
        # A spam ONLY until title screen appears
        if not title_appeared and frame % 10 == 0:
            emu.press_button("a", frames=1)
        
        emu.tick(1)
        frame += 1
        
except KeyboardInterrupt:
    print("\n\n✅ Stopped")

finally:
    emu.close()
