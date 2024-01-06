def solution(x):
    
    def is_jumping_num(x):
        str_x = str(x)
        for i in range(len(str_x) - 1):
            if abs((int(str_x[i])) - int(str_x[i + 1])) != 1:
                return False
        return True
    
    jumping_numbers = [num for num in x if is_jumping_num(num)]

    return jumping_numbers