def solution(inputArray):
    
    long_str = 0
    str_list = []
    for i in range(len(inputArray)):
        if len(inputArray[i]) > long_str:
            long_str = len(inputArray[i])
            str_list = [inputArray[i]]
        elif len(inputArray[i]) == long_str:
            str_list.append(inputArray[i])         
        else:
            pass
    return str_list