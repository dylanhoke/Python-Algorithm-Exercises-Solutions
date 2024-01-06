class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(head, value, index) -> ListNode:
    newNode = ListNode(value)
    if index <= 0:
        newNode.next = head
        return newNode
        
    if head is None:
        return newNode
    
    current = head
    prev = None
    count = 0
    
    while current is not None and count < index:
        prev = current
        current = current.next
        count += 1
    
    prev.next = newNode
    newNode.next = current
    
    return head