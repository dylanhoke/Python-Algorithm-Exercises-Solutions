from collections import Counter

def solution(s:str) -> str:

    """
    loop throguh our string to keep count of uniqueness
        build our dictionary (char:count)

    loop throguh our string AGAIN

    return the first character where the count is 1

    """
    count = {}
    #counter = Counter(s)


    for char in s:
        if char not in count:

            count[char] = 0

        count[char] += 1

    #^^^Counter is this function above^^^
        

    for char in s:
        if count[char] == 1:
            return char
        
    return '_'