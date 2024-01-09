def solution(connections):
    visited = set()
    def dfs(start, parent):
        if start in visited:
            return True
        visited.add(start)
        for neighbor in connections[start]:
            if neighbor != parent:
                cyclic = dfs(neighbor, start)
                if cyclic:
                    return True
        visited.remove(start)
        return False
    for node in range(len(connections)):
        detectCycle = dfs(node, None)
        if detectCycle:
            return True 
    return False