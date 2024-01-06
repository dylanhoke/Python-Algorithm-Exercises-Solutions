def solution(connections:list[list[int]]) -> bool:

    visited = set()

    def dfs(start:int) -> bool:
        #depth first search
        if start in visited:
            #if you already have it
            return True
        
        visited.add(start)

        for neighbor in connections[start]:

            if dfs(neighbor):
                
                return True
            
        visited.remove(start)

        return False

    for node in range(len(connections)):

        if dfs(node):
            return True
        
    return False