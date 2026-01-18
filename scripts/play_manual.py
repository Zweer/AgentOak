#!/usr/bin/env python3
"""Play Pokémon manually and save states at key points."""

import signal
import sys
from pathlib import Path

from agentoak.emulator import GameBoyEmulator


# Global emulator reference for signal handler
_emulator = None
_is_test_mode = False
_save_name = None


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully."""
    global _emulator, _is_test_mode, _save_name
    print("\n\n💾 Saving state...")
    
    if _emulator and _save_name:
        if _is_test_mode:
            # Test mode: save to tests/fixtures/
            save_dir = Path("tests/fixtures")
            save_dir.mkdir(parents=True, exist_ok=True)
            save_path = save_dir / f"{_save_name}.state"
            screenshot_path = save_dir / f"{_save_name}.png"
        else:
            # Normal mode: save to saves/
            save_dir = Path("saves")
            save_dir.mkdir(parents=True, exist_ok=True)
            save_path = save_dir / f"{_save_name}.state"
            screenshot_path = Path("screenshots") / f"{_save_name}.png"
            Path("screenshots").mkdir(exist_ok=True)
        
        try:
            _emulator.save_state(str(save_path))
            print(f"✓ Saved to {save_path}")
            
            _emulator.save_screenshot(str(screenshot_path))
            print(f"✓ Screenshot saved to {screenshot_path}")
            
            # If test mode, generate JSON spec
            if _is_test_mode:
                print("\n📝 Generating test specification...")
                import subprocess
                result = subprocess.run([
                    "uv", "run", "python", "scripts/extract_test_spec.py",
                    str(save_path),
                    f"Test save: {_save_name}"
                ], capture_output=True, text=True)
                
                if result.returncode == 0:
                    print("✓ Test spec generated")
                    print(f"\n📋 Next steps:")
                    print(f"  1. Add '{_save_name}' to SAVE_STATES in tests/test_memory_reading.py")
                    print(f"  2. Run: make test")
                else:
                    print(f"⚠️  Failed to generate spec: {result.stderr}")
            
        except Exception as e:
            print(f"⚠️  Error saving: {e}")
        finally:
            _emulator.close()
    
    print("\n✅ Done!")
    sys.exit(0)


def main():
    """Run game with display and allow manual saving."""
    global _emulator, _is_test_mode, _save_name
    
    print("🎮 Manual Play Mode")
    print("=" * 60)
    
    # Ask if this is for testing
    test_input = input("Generate test fixture? (y/n): ").strip().lower()
    _is_test_mode = test_input == 'y'
    
    if _is_test_mode:
        print("\n📋 Test Mode: Save will go to tests/fixtures/")
        print("   A JSON spec will be auto-generated")
    else:
        print("\n💾 Normal Mode: Save will go to saves/")
    
    # Ask for save name
    _save_name = input("\nSave state name (e.g., 'bulbasaur'): ").strip()
    if not _save_name:
        _save_name = "manual"
    
    print(f"\n🎮 Loading Pokémon Blue...")
    print("Play in the window, then press Ctrl+C here to save.\n")
    
    # Register signal handler
    signal.signal(signal.SIGINT, signal_handler)
    
    _emulator = GameBoyEmulator("roms/pokemon-blue.gb", headless=False)
    
    try:
        # Run game loop
        while True:
            _emulator.tick()
    except KeyboardInterrupt:
        # Should be caught by signal handler, but just in case
        signal_handler(None, None)


if __name__ == "__main__":
    main()
