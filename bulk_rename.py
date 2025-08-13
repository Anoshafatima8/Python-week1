import os
import argparse
from pathlib import Path
from datetime import datetime

def bulk_rename_images(directory):
    directory = Path(directory)

    if not directory.exists():
        print(f" Directory '{directory}' not found.")
        return

    counter = 1
    for file in directory.iterdir():
        if file.is_file() and file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            # Get creation time
            creation_time = file.stat().st_ctime
            date_str = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d")

            # New filename
            new_name = f"{date_str}_{counter}{file.suffix.lower()}"
            new_path = directory / new_name

            os.rename(file, new_path)
            print(f"Renamed: {file.name} → {new_name}")
            counter += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk rename image files by creation date.")
    parser.add_argument("directory", help="Path to the folder containing images.")
    args = parser.parse_args()

    bulk_rename_images(args.directory)
