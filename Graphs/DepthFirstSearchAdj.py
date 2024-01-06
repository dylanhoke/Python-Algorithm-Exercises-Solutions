from collections import deque

class ListNode:

    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def solution(adj_list:list[ListNode], start:ListNode) -> list[ListNode]:

    visited = {} # set()

    stack = deque()

    stack.append(start.value)

    # while len(stack) != 0:
    while stack:

        toVisit = stack.pop()

        if toVisit in visited:

            continue

        # visited.add(toVisit)
        visited.add(toVisit)

        for neighbor in adj_list[toVisit]:

            stack.append(neighbor.value)

    return list(visited)
    
