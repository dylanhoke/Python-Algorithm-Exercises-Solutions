def solution(a):
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - i - 1):
            #don't use a modern style generaly hard code it

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
            
        if not swapped:
            return a
    return a