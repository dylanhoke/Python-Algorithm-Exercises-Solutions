class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(head):
    if head is None:
        return head
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev