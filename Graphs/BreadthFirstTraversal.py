from collections import deque

def solution(adj_list, start):

    if start not in adj_list:
        return []
    visited = set()
    queue = deque()
    result = []
    queue.append(start)
    while queue: 
        node = queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
            for neighbor in adj_list.get(node, []):  
                if neighbor not in visited:
                    queue.append(neighbor)
    return result