def solution(names):
    
    
    name_dict = {}
    
    result = []
    
    for name in names:
        
        if name not in name_dict:
            
            name_dict[name] = 1
            
            result.append(name)
            
        else:
            
            while True:
                
                new_name = f"{name}({name_dict[name]})"
                
                if new_name not in name_dict:
                    
                    break
                    
                name_dict[name] += 1
                
            name_dict[new_name] = 1
            
            result.append(new_name)
            
    return result