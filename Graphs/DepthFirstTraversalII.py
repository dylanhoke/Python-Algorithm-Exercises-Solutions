from collections import deque


def solution(adj_list, start):
        
    visited = set()
    
    stack = deque()
    
    stack.append(start)
    
    result = []
    
    while stack:
        
        toVisit = stack.pop()
        
        if toVisit not in visited:
            
            visited.add(toVisit)
            
            result.append(toVisit)
            
            stack.extend(neighbor for neighbor in adj_list[toVisit] if neighbor not in visited)
            
    return result