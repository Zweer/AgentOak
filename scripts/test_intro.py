#!/usr/bin/env python3
"""Test intro sequence automation."""

import signal
import sys

from agentoak.emulator import GameBoyEmulator
from agentoak.intro import run_intro_sequence

ROM_PATH = "roms/pokemon-blue.gb"

# Global emulator reference for signal handler
emu = None


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully."""
    print("\n\n🛑 Interrupted by user")
    if emu:
        emu.close()
    sys.exit(0)


# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

# Start emulator with display
emu = GameBoyEmulator(ROM_PATH, headless=False)

# Run intro sequence
try:
    run_intro_sequence(emu, starter="bulbasaur", use_preset_names=True)
    
    # Save state after intro
    emu.save_state("saves/after_intro.state")
    print("\n✅ Intro complete! State saved to saves/after_intro.state")
    
    # Keep window open
    input("\nPress Enter to close...")
    
finally:
    emu.close()
