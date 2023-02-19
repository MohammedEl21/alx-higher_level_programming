#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""

import sys
from os import path
from typing import List

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item(args: List[str]) -> List[str]:
    """Add all arguments to a list and return it"""
    try:
        items = load_from_json_file("add_item.json")
    except:
        items = []

    items.extend(args)
    save_to_json_file(items, "add_item.json")
    return items


if __name__ == "__main__":
    add_item(sys.argv[1:])
