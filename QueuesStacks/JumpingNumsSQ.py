def solution(x):
    # for i in range(x):
    #     i = str(i)
    #     if int(i[0]) == int(i[1]) + 1 or int(i[1]) == int(i[0]) + 1:
    #         jumping.append(int(i))
    #     elif len(i) == 1:
    #         jumping.append(int(i))
    # return jumping
    #####################################################
    # count = 0
    # for i in range(x - 1):
    #     i = str(i)
    #     if int(i[0]) == count:
    #         for j in range(9):
    #             if int(i[0]) == j + 1:
    #                 jumping.append(int(i))
    #         count += 1

    # return jumping
    def jumping_func(x):
        str_x = str(x)
        for i in range(len(str_x) - 1):
            if abs((int(str_x[i])) - int(str_x[i + 1])) != 1:
                return False
        return True
    
    jumping = [[] for _ in range(10)]
    
    for i in range(x + 1):
        if jumping_func(i):
            first_digit = int(str(i)[0])
            jumping[first_digit].append(i)
    
    result = []
    
    for digit_list in jumping:
        result.extend(digit_list)
    return result