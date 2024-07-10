# convert heic to PNG

import os
import subprocess
import sys


def heic_to_png(input_file, output_file):
    try:
        subprocess.run(
            ["sips", "-s", "format", "png", input_file, "--out", output_file],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)


for i in [i for i in os.listdir() if i.split(".")[-1].lower() == "heic"]:
    heic_to_png(i, i.split(".")[0] + ".png")
    print(f"Converted {i} to {i.split('.')[0]}.png")
