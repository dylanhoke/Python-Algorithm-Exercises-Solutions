from collections import deque

class ListNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def solution(adj_list:list[ListNode], start:ListNode) -> list[ListNode]:
    visited = set()
    Dq = deque()
    Dq.append(start)
    while Dq:
        toVisit = Dq.pop()
        if toVisit in visited:
            continue
        visited.add(toVisit)
        for neighbor in adj_list[toVisit.value]:
            Dq.append(neighbor)
    return list(visited)