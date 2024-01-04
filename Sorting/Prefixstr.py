def solution(strings, sources):
    
    
    result = []
    
    for source in sources:
        
        prefix = False
        
        cur = ""
        
        for string in strings:
            
            cur += string
            
            if cur == source:
                
                prefix = True
                
                break
                
        result.append(prefix)
        
    return result