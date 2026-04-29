import subprocess
import sys
import os

def convert_video(input_file, output_file):
    if not os.path.exists(input_file):
        print("File not found!")
        return

    command = [
        "ffmpeg",
        "-i", input_file,
        output_file
    ]

    try:
        subprocess.run(command, check=True)
        print("Conversion successful!")
    except subprocess.CalledProcessError:
        print("Conversion failed!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py input.mp4 output.mp3")
    else:
        convert_video(sys.argv[1], sys.argv[2])
