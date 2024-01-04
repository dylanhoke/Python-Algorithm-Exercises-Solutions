# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
# def solution(head, index):
#     if head is None or index == 0:
#         return head.next
    
#     if index < 0:
#         return None

#     current = head
#     prev = None
#     count = 0
    
#     while current is not None and count < index:
#         prev = current
#         current = current.next
#         count += 1
    
#     if current is not None:
#         prev.next = current.next
#     return head

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(head, index):
    if head is None:
        return head.next
    if index < 0:
        return None

    if index == 0:
        return head.next
        
    current = head
    prev = None
    count = 0
    
    while current is not None and count < index:
        prev = current
        current = current.next
        count += 1
        
    if count == index and current is not None:
        prev.next = current.next
    elif count <= index:
        return None
        
    return head 