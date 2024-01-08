from collections import deque

def solution(adj_list, start):    
    visited = set()
    Dq = deque()
    Dq.append(start)
    result = []
    while Dq: 
        toVisit = Dq.pop()
        if toVisit not in visited:
            visited.add(toVisit)
            result.append(toVisit)
            Dq.extend(neighbor for neighbor in adj_list[toVisit] if neighbor not in visited)    
    return result