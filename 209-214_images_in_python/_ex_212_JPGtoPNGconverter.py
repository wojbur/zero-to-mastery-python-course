"""
Script to convert JPEG files into PNG. It accepts two command line arrguments:
- First arg is a path to directory containing JPEG files
- Second arg is a path to save converted PNG files to
"""

import sys
import os
from pathlib import Path
from PIL import Image


# Grab the first and second argument
try:
    jpg_dir, png_dir = sys.argv[1], sys.argv[2]
except IndexError:
    print('Provide arguments: jpg directory and png direcory')
    quit()

# Check if the first argument points to existing directory
if not os.path.exists(jpg_dir):
    print('First argument must point to existing directory')
    quit()

# Check if new folder exist, if not create it
if not os.path.exists(png_dir):
    os.mkdir(png_dir)

# Loop through Pokedex
for filename in os.listdir(jpg_dir):
    file = os.path.join(jpg_dir, filename)
    # check if it is a jpeg file
    if os.path.isfile(file) and os.path.splitext(
            file)[-1].lower() in ['.jpg', '.jpeg']:
        img = Image.open(file)
        # convert file to png and save
        png_filename = Path(file).stem + '.png'
        save_dir = os.path.join(png_dir, png_filename)
        img.save(save_dir, 'png')
