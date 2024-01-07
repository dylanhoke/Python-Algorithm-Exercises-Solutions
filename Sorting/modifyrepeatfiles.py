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

from collections import defaultdict

# def solution(names):
#     name_count = defaultdict(int)
#     result = []

#     for name in names:
#         new_name = name
#         count = name_count[name]

#         while new_name in name_count:
#             count += 1
#             new_name = f"{name}({count})"

#         name_count[name] = count
#         name_count[new_name] += 1
#         result.append(new_name)

#     return result