import glob
import os
import shutil
import time
import logging
from pathlib import Path
from typing import List

from PIL import Image

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def get_image_files(pattern: str = "**/*.jpg", recursive: bool = True) -> List[str]:
    """Return a list of image file paths matching a glob pattern."""
    files = glob.glob(pattern, recursive=recursive)
    logging.info("Found %d image files", len(files))
    return files


def ensure_directory(parent_dir: str, directory: str) -> str:
    """Create a directory inside parent_dir if it doesn’t exist. Return full path."""
    path = Path(parent_dir) / directory
    path.mkdir(parents=True, exist_ok=True)
    return str(path)


def copy_files(indexes: List[int], file_list: List[str], dest: str, prefix: str = "RImage") -> None:
    """Copy selected files to destination and log their original locations."""
    timestamp = int(time.time())
    log_file = Path(dest) / f"original_file_loc_{timestamp}.txt"

    with open(log_file, "w", encoding="utf-8") as f:
        for idx in indexes:
            src = Path(file_list[idx])
            dst = Path(dest) / f"{prefix}{idx}{src.suffix}"
            f.write(f"{prefix}{idx}: {src.resolve()}\n")
            shutil.copy(src, dst)

    logging.info("Copied %d files to %s", len(indexes), dest)


def is_horizontal(filepath: str) -> bool:
    """Return True if image width > height, False otherwise."""
    try:
        with Image.open(filepath) as img:
            width, height = img.size
            return width > height
    except Exception as e:
        logging.warning("Failed to open image %s: %s", filepath, e)
        return False
