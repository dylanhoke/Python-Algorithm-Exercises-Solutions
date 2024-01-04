from collections import deque

class ListNode:

    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def solution(ad_list:list[ListNode], start:ListNode) -> list[ListNode]:

    """
    initialize visited set to empty

    initialize stack

    add first node to stack

    while stack isnt empty
        pop the next node

        check visited
            
            skip

        mark visited

        add neighbors to stack
    """

    visited = {} # set()

    stack = deque()

    stack.append(start)

    # while len(stack) != 0:
    while stack:

        toVisit = stack.pop()

        if toVisit in visited:

            continue

        # visited.add(toVisit)
        visited[toVisit] = True

        for neighbor in ad_list[toVisit]:

            stack.append(neighbor)

    return list(visited)
    
