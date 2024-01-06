class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
    

class ListStack:

    def __init__(self):
        self.head = None
        self.size = 0
    
    def pop(self):
        if self.size < 1:
            return None
        popped = self.head
        self.head = self.head.next
        popped.next = None
        self.size -= 1
        return popped.value

    def push(self, item: str):
        toPush = Node(item)
        toPush.next = self.head
        self.head = toPush
        self.size += 1
        return toPush.value

    # def __bool__(self):
    #     if self.size == 0:
    #         return False
    #     return True
    
class Stack:

    def __init__(self):
        self.stack = []
    
    def pop(self) -> str:
        return self.stack.pop()

    def push(self, item: str):
        return self.stack.append(item)

def solution(sequence: str) -> bool:

    if sequence is None or len(sequence) == 1:
        return False
    
    stack = ListStack()

    # if char == "(" and popped == ")"

    matchMap = {
        "{":"}",
        "(":")",
        "[":"]"
    }

    for char in sequence:
        #if char is an open bracket
        if char in matchMap:
            stack.push(char)
        else:
            if not stack:
                return False
            
            popped = stack.pop()

            # if current closing bracket is not the closing bracket of popped
            if char != matchMap[popped]:
                return False
            
    return not stack
