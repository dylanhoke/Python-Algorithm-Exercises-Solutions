def solution(a, value):

    for index, ele in enumerate(a):
        if value == ele:
            return index
    # for index in range(len(a)):
    #     if value == a[index]:
    #         return index
    return False