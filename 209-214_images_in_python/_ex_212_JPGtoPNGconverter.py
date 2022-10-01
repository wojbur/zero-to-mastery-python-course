"""
Script to convert JPEG files into PNG. It accepts two command line arrguments:
- First arg is a path to directory containing JPEG files
- Second arg is a path to save converted PNG files to
"""

from msilib.schema import Error
import sys
import os
from PIL import Image

# Grab the first and second argument
try:
    jpg_dir, png_dir = sys.argv[1], sys.argv[2]
except IndexError:
    print('Provide arguments: jpg folder and png folder')
    quit()

# Check if the first argument points to existing directory
if not os.path.exists(jpg_dir):
    print('First argument must point to existing directory')
    quit()

# Check if new folder exist, if not create it
if not os.path.exists(png_dir):
    os.mkdir(png_dir)

# Loop through Pokedex

# Convert images to png

# Save to the new folder