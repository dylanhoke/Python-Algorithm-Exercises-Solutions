def solution(s1, s2):
    def count(s):  
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        return counts     
    counts1 = count(s1)
    counts2 = count(s2)
    result = []
    s1_index = s2_index = 0
    while s1_index < len(s1) and s2_index < len(s2):
        char1 = s1[s1_index]
        char2 = s2[s2_index]
        if counts1[char1] < counts2[char2] or (counts1[char1] == counts2[char2] and char1 < char2):

            result.append(char1)
            s1_index += 1
        elif counts1[char1] > counts2[char2]:
            result.append(char2)
            s2_index += 1
        else:
            if char1 < char2:
                result.append(char1)
                s1_index += 1
            else:
                result.append(char2)
                s2_index += 1      
    result.extend(s1[s1_index:])
    result.extend(s2[s2_index:])
    return ''.join(result)

# from collections import defaultdict
# def solution(s1, s2):
#     def count(s):
#         counts = defaultdict(int)
#         for char in s:
#             counts[char] += 1
#         return counts
#     counts1 = count(s1)
#     counts2 = count(s2)
#     result = []
#     s1_index = s2_index = 0
#     while s1_index < len(s1) and s2_index < len(s2):
#         char1, char2 = s1[s1_index], s2[s2_index]
#         if (counts1[char1], char1) < (counts2[char2], char2):
#             result.append(char1)
#             s1_index += 1
#         else:
#             result.append(char2)
#             s2_index += 1
#     result.extend(s1[s1_index:])
#     result.extend(s2[s2_index:])
#     return ''.join(result)