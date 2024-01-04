def solution(a):
    
    
    count = 0
    
    for i in range(len(a)):

        for j in range(i+1, len(a)):
            
            sum_ = a[i] + a[j]
            
            if sum_ in a:

                count += 1

    return count