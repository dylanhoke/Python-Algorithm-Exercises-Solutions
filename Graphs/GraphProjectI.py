def solution(connections:list[list[int]]) -> bool:


    visited = set()

    def dfs(start:int) -> bool:
        #depth first search
        if start in visited:
            #if you already have it
            return True
        
        visited.add(start)

        for neighbor in connections[start]:

            cyclic = dfs(neighbor)

            if cyclic:
                
                return True
            
        visited.remove(start)

        return False

    for node in range(len(connections)):

        detectCycle = dfs(node)

        if detectCycle:
            return True
        
    return False