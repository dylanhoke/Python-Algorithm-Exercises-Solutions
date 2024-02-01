def solution(s1, s2):
    common_chars = set(s1) & set(s2)
    
    solution = sum(min(s1.count(char), s2.count(char)) for char in common_chars)
    return solution