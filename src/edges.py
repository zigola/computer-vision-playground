"""Minimal edge-detection command-line example."""

from __future__ import annotations

import argparse
from pathlib import Path

import cv2


def detect_edges(input_path: Path, output_path: Path) -> None:
    image = cv2.imread(str(input_path), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Could not read image: {input_path}")
    edges = cv2.Canny(image, 100, 200)
    if not cv2.imwrite(str(output_path), edges):
        raise OSError(f"Could not write image: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path)
    parser.add_argument("--output", type=Path, default=Path("edges.png"))
    args = parser.parse_args()
    detect_edges(args.image, args.output)
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
