def solution(inputString):
    
    
    char_count = {}
    
    for char in inputString:
        
        if char in char_count:
            
            char_count[char] += 1
            
        else:
            
            char_count[char] = 1
    
    prev_char = None
    
    for char in sorted(char_count.keys()):
        
        if prev_char is not None:
            
            if ord(char) - ord(prev_char) > 1 or char_count[char] > char_count[prev_char]:
                
                return False
                
        prev_char = char
        
    return True

#this program does not account for bbc or zyy