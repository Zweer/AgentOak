#!/usr/bin/env python3
"""Find exact rows with 'Blue Version' text and monitor left edge."""

import signal
import sys

from agentoak.emulator import GameBoyEmulator
from agentoak.game_state import is_at_title_screen

ROM_PATH = "roms/pokemon-blue.gb"

emu = None


def signal_handler(sig, frame):
    print("\n\n🛑 Interrupted")
    if emu:
        emu.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

emu = GameBoyEmulator(ROM_PATH, headless=False)

print("🎮 Finding 'Blue Version' text rows")
print("A spam until title screen, then STOP and analyze\n")

frame = 0
title_appeared = False

try:
    while frame < 3600:
        at_title = is_at_title_screen(emu)
        
        if at_title and not title_appeared:
            title_appeared = True
            print(f"\n🎯 Title screen at frame {frame}! Stopping A spam.\n")
            print("Now monitoring for 'Blue Version' text...\n")
        
        # A spam only until title appears
        if not title_appeared and frame % 10 == 0:
            emu.press_button("a", frames=1)
        
        # After title appears, analyze every 10 frames
        if title_appeared and frame % 10 == 0:
            screen = emu.pyboy.screen.ndarray
            
            # Scan rows 40-70 to find text
            print(f"\n[Frame {frame} - {frame//60}s {frame%60:02d}f]")
            
            for row in range(40, 70, 2):
                # Check full width for dark pixels
                row_data = screen[row, :, 0]
                dark_count = (row_data < 150).sum()
                
                if dark_count > 5:  # Row has some text
                    # Check left edge (first 60 pixels)
                    left_edge = screen[row, 0:60, 0]
                    left_white = (left_edge > 200).sum()
                    left_dark = (left_edge < 150).sum()
                    
                    # Show ASCII of this row
                    ascii_row = "".join("█" if p < 150 else " " for p in row_data[::4])
                    
                    print(f"  Row {row:2d}: Dark={dark_count:3d} | "
                          f"Left: White={left_white:2d} Dark={left_dark:2d} | "
                          f"{ascii_row[:40]}")
        
        emu.tick(1)
        frame += 1
        
except KeyboardInterrupt:
    print("\n\n✅ Stopped")

finally:
    emu.close()
