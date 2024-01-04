def solution(a):
    
    for i in range(len(a)):
        cur = a[i]
        j = i - 1
        
        while j >=0 and cur < a[j]:
            a[j+1] = a[j]
            j -= 1
        
        a[j+1] = cur
        
    return a