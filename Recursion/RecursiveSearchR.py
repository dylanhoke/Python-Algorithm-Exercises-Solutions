class ListNode(object):
    def __init__(self,x):
        self.value = x
        self.next = None

def solution(head:ListNode, value:int) -> bool:
    #start with your base case and reducing case
    #iteratively: for(start;end;how we get from start to end)
    #base cases:
        #head does not exist
        #head is our value
    #reducing case:
        #we are checking every node head.next
    
    if head is None:
        return False
    
    if head.value == value:
        return True
    
    return solution(head.next, value)
