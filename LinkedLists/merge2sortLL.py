class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(l1, l2):
    head = ListNode(None)
    current = head
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
        
    if l2:
        current.next = l2
    if l1:
        current.next = l1
        
    return head.next