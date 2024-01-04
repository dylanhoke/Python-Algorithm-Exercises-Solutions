class Stack:
    
    def __init__(self):
        self.stack = []
        # self.temp = []
 
    def push(self, item: str):
        return self.stack.append(item)
 
    def pop(self) -> str:
        return self.stack.pop()
    
    def __len__(self):
        return len(self.stack)
    
    # def temp(self, item: str):
    #     return self.temp.append(item)
        
def solution(sequence: str) -> bool:
    
    if sequence is None:
        return False
    
    if len(sequence) == 1:
        return False
    
    dictionary = {
        '(':')',
        '{':'}',
        '[':']'
    }

    stack = Stack()
    
    for char in sequence:
        if char in dictionary:
            stack.push(char)
        else:
            if not stack:
                return False

            popped = stack.pop()
            
            if char != dictionary[popped]:
                return False

    return True