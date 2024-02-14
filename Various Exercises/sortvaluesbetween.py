def solution(a):
    height_list = []
    ans_list = []
    for i in a:
        if i > 0:
            height_list.append(i)
            
    height_list.sort()
    
    for i in a:
        if i < 0:
            ans_list.append(i)
        else:
            ans_list.append(height_list.pop(0))
    return ans_list