class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

# def solution(head, value, index) -> ListNode:
#     newNode = ListNode(value)
#     if head is None:
#         head = newNode = ListNode(value)
#         return head
    
#     count = 0
#     node = head
#     while node is not None:
#         count += 1
#         node = node.next
#         # print(count)
        
#     if index <= 0:
#         # newNode = ListNode(value)
#         newNode.next = head
#         return newNode
#     elif index >= count:
#         # newNode = ListNode(value)
#         p = head
#         while p.next:
#             p = p.next
#         p.next = newNode
#         return head
#     else:
#         # newNode = ListNode(value)
#         new_head = head
#         old_head = head
#         counter = index-1
#         while counter != 0:
#             counter -= 1
#             new_head = new_head.next
#             old_head = old_head.next.next
#         newNode.next = new_head.next
#         new_head.next = newNode
#         return head


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