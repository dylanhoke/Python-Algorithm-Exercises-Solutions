def solution(n):
    split = str(n)
    midpoint = len(split) // 2
    
    first_half = split[:midpoint]
    second_half = split[midpoint:]
    first_sum = 0
    second_sum = 0
    
    for i in first_half:
        first_sum += int(i)
    
    for i in second_half:
        second_sum += int(i)
    
    if first_sum == second_sum:
        return True
    
    return False