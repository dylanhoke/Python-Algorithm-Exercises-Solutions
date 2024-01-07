def solution(a):
    
    
    mean_indices = [(sum(arr) / len(arr), i) for i, arr in enumerate(a)]
    
    mean_indices.sort(key = lambda x: (x[0], a[x[1]]))
    
    groups = []
    
    cur_group = []
    
    cur_mean = mean_indices[0][0]
    
    for mean, index in mean_indices:
        
        if mean == cur_mean:
            
            cur_group.append(index)
            
        else:
            
            groups.append(sorted(cur_group))
            
            cur_group = [index]
            
            cur_mean = mean
            
    groups.append(sorted(cur_group))
    
    return sorted(groups)

# for i in range(len(mean_indices)):
#         mean, index = mean_indices[i]

#         if i > 0 and mean != mean_indices[i - 1][0]:
#             groups.append(sorted(cur_group))
#             cur_group = [index]
#         else:
#             cur_group.append(index)