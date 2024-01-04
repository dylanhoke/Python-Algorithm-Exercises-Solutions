def solution(connections):
    
    
    visited = set()
    
    def dfs(start):
        
        if start in visited:
            
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