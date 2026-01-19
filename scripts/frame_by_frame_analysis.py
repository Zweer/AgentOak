#!/usr/bin/env python3
"""Detailed frame-by-frame analysis from 7s to 10s."""

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


def screen_to_ascii(screen, scale=4):
    """Convert screen to ASCII art."""
    height, width = screen.shape[:2]
    lines = []
    for y in range(0, height, scale):
        line = ""
        for x in range(0, width, scale):
            pixel = screen[y, x, 0]
            if pixel == 0:
                line += "█"
            elif pixel < 100:
                line += "▓"
            elif pixel < 200:
                line += "▒"
            else:
                line += " "
        lines.append(line)
    return "\n".join(lines)


signal.signal(signal.SIGINT, signal_handler)

emu = GameBoyEmulator(ROM_PATH, headless=False)

print("🎮 Frame-by-frame analysis from 7s to 10s")
print("A spam until 7s, then NO A spam\n")

frame = 0
output_file = open("frame_analysis.log", "w")

try:
    while frame < 600:  # 10 seconds
        # A spam only until 7 seconds
        if frame < 420 and frame % 10 == 0:
            emu.press_button("a", frames=1)
        
        # From 7s to 10s, log every frame
        if 420 <= frame < 600:
            at_title = is_at_title_screen(emu)
            has_version = title_screen_has_version_text(emu)
            
            screen = emu.pyboy.screen.ndarray
            
            # Sample the Version text region
            text_region = screen[48:54, 60:100, 0]
            dark_pixels = (text_region < 150).sum()
            
            output_file.write(f"\n{'='*60}\n")
            output_file.write(f"Frame {frame} ({frame//60}s {frame%60:02d}f)\n")
            output_file.write(f"Title: {at_title} | Version: {has_version} | Dark pixels: {dark_pixels}\n")
            output_file.write(f"{'='*60}\n")
            output_file.write(screen_to_ascii(screen))
            output_file.write("\n")
            output_file.flush()
            
            if frame % 60 == 0:
                print(f"[{frame//60}s] Logged frame {frame}")
        
        emu.tick(1)
        frame += 1
        
except KeyboardInterrupt:
    print("\n\n✅ Stopped")

finally:
    output_file.close()
    print("\n✅ Analysis saved to: frame_analysis.log")
    emu.close()
