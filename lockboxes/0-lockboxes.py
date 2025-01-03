#!/usr/bin/python3
"""
Determines if all boxes can be unlocked.
"""
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): List of lists where each sublist contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is unlocked

    keys = boxes[0]  # Start with the keys in the first box

    for key in keys:
        if 0 <= key < n and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])

    return all(opened)

if __name__ == "__main__":
    # Example usage
    boxes = [[1], [2], [3], []]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 3], [3, 0, 1], [2], [0]]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 2, 3], [], [4], [5], []]
    print(canUnlockAll(boxes))  # Output: False