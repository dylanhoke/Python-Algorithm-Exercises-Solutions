def solution(sequence):
    """
    Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
    """
    removed_element = False
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            if removed_element:
                return False
            if i >= 2 and sequence[i] <= sequence[i - 2]:
                sequence[i] = sequence[i - 1]
            removed_element = True
    return True

