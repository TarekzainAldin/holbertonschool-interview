#!/usr/bin/python3
"""Module to determine if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each sublist contains keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n  # Tracks the status of opened boxes
    opened[0] = True  # The first box is always open
    keys = boxes[0]  # Start with the keys from the first box

    while keys:
        key = keys.pop()
        if 0 <= key < n and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])  # Add keys from the newly opened box

    return all(opened)
