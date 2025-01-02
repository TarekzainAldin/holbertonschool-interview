def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: List of lists, where each inner list contains keys for other boxes.
    :return: True if all boxes can be opened, else False.
    """
    n = len(boxes)  # Number of boxes
    opened = [False] * n  # Keep track of opened boxes
    opened[0] = True  # The first box is unlocked

    keys = [0]  # Start with the keys from the first box

    while keys:
        current_key = keys.pop()  # Take a key

        # If the box corresponding to this key hasn't been opened yet
        if not opened[current_key]:
            opened[current_key] = True  # Mark the box as opened

            # Add all the keys inside this box to the keys list
            for key in boxes[current_key]:
                if 0 <= key < n and not opened[key]:
                    keys.append(key)

    # Check if all boxes have been opened
    (opened)

# Example usage:
if __name__ == "__main__":
   boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
