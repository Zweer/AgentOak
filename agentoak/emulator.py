"""PyBoy emulator wrapper for Pokémon Red/Blue."""

from pathlib import Path
from typing import Literal

import numpy as np
from pyboy import PyBoy


class GameBoyEmulator:
    """Wrapper around PyBoy for Pokémon games."""

    def __init__(
        self,
        rom_path: str | Path,
        headless: bool = True,
    ):
        """Initialize the emulator.
        
        Args:
            rom_path: Path to the ROM file
            headless: Run without display window
        """
        self.rom_path = Path(rom_path)
        if not self.rom_path.exists():
            raise FileNotFoundError(f"ROM not found: {rom_path}")
        
        window = "null" if headless else "SDL2"
        self.pyboy = PyBoy(str(self.rom_path), window=window)
        
        # Try to get game wrapper if available
        try:
            self.game_wrapper = self.pyboy.game_wrapper
        except AttributeError:
            self.game_wrapper = None
        
    def tick(self, count: int = 1) -> None:
        """Advance emulation by N frames."""
        for _ in range(count):
            self.pyboy.tick()
    
    def press_button(self, button: str, frames: int = 1) -> None:
        """Press a button for N frames.
        
        Args:
            button: Button name (a, b, start, select, up, down, left, right)
            frames: Number of frames to hold
        """
        self.pyboy.button_press(button)
        self.tick(frames)
        self.pyboy.button_release(button)
    
    def read_memory(self, address: int, length: int = 1) -> bytes:
        """Read bytes from memory.
        
        Args:
            address: Memory address (0x0000-0xFFFF)
            length: Number of bytes to read
            
        Returns:
            Bytes read from memory
        """
        return bytes(self.pyboy.memory[address:address + length])
    
    def get_walkable_matrix(self) -> np.ndarray:
        """Get walkable tiles matrix for current screen.
        
        Returns:
            2D numpy array where 1 = walkable, 0 = blocked
        """
        if self.game_wrapper and hasattr(self.game_wrapper, "game_area_collision"):
            collision = self.game_wrapper.game_area_collision()
            return collision.astype(np.uint8)
        return np.zeros((18, 20), dtype=np.uint8)
    
    def save_state(self, path: str | Path) -> None:
        """Save emulator state to file."""
        with open(path, "wb") as f:
            self.pyboy.save_state(f)
    
    def load_state(self, path: str | Path) -> None:
        """Load emulator state from file."""
        with open(path, "rb") as f:
            self.pyboy.load_state(f)
    
    def close(self) -> None:
        """Close the emulator."""
        self.pyboy.stop()
