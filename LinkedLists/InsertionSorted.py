class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None
def solution(l, value):
    newNode = ListNode(value)
    if l is None:
        l = newNode = ListNode(value)
        return l
    if l.value > value:
        newNode.next = l
        return newNode
    current = l
    while current.next is not None and current.next.value <= value:
        current = current.next
    newNode.next = current.next
    current.next = newNode
    return l