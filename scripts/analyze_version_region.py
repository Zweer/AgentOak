#!/usr/bin/env python3
"""Analyze the 'Blue Version' text region to find correct threshold."""

from PIL import Image
import numpy as np

# Load the screenshot with "Blue Version" visible
img = Image.open("debug_menu_detected.png")
arr = np.array(img)

print("Analyzing 'Blue Version' text region\n")

# Try different regions to find where the text is
for start_row in range(48, 58, 2):
    for end_row in range(start_row + 6, start_row + 12, 2):
        region = arr[start_row:end_row, 60:100, 0]
        dark_pixels = (region < 150).sum()
        
        if dark_pixels > 5:
            print(f"Row {start_row:2d}-{end_row:2d}: {dark_pixels:3d} dark pixels")
            
            # Show ASCII
            print("  ", end="")
            for row in region[::2]:  # Every other row
                line = "".join("█" if p < 150 else " " for p in row[::2])
                print(line[:20])
                print("  ", end="")
            print()
