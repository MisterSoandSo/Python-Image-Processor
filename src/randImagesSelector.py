#!/usr/bin/env python3
import os
import random
import json
from pathlib import Path

from backend import get_image_files, ensure_directory, copy_files

LAST_SELECTION_FILE = "last_selection.json"


def load_last_selection() -> list[int]:
    """Load the most recent selection from disk if it exists."""
    if Path(LAST_SELECTION_FILE).exists():
        with open(LAST_SELECTION_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_selection(indexes: list[int]) -> None:
    """Save the current selection to disk."""
    with open(LAST_SELECTION_FILE, "w", encoding="utf-8") as f:
        json.dump(indexes, f)


def get_fresh_selection(total: int, num_images: int, last_selection: list[int]) -> list[int]:
    """Generate a random sample that isn’t identical to the last selection."""
    if num_images > total:
        raise ValueError(f"Requested {num_images} images, but only {total} found.")

    while True:
        selection = random.sample(range(total), num_images)
        if selection != last_selection:  # avoid exact repeat
            return selection


def main():
    num_images = 4000
    file_list = get_image_files()
    total = len(file_list)

    last_selection = load_last_selection()
    selected_indexes = get_fresh_selection(total, num_images, last_selection)

    print(f"Randomly selected {num_images} images out of {total}")
    dest = ensure_directory(os.getcwd(), "RandSelect")
    copy_files(selected_indexes, file_list, dest)

    save_selection(selected_indexes)


if __name__ == "__main__":
    main()
