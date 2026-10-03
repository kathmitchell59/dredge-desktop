"""Dredge Desktop — A local helper for DREDGE boat folders, fish notes, and fog photos."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='dredge_desktop',
        description='A local helper for DREDGE boat folders, fish notes, and fog photos.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Dredge Desktop')
    print('Keep the boat on disk before a night voyage.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
