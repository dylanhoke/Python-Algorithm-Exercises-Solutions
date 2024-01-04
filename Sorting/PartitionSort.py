def solution(a, pivot):
    
    left = []
    right = []
    
    for num in a:
        if num >= pivot:
            right.append(num)
        elif num < pivot:
            left.append(num)
            
    return left, right