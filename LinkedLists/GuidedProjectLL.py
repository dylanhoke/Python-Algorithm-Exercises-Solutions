class ListNode(object):
    def __inti__(self, x):
        self.value = x
        self.next = None

def solution(head:ListNode, value:int, index:int) -> ListNode:

    if head is None:
        head = ListNode(value)
        return head
    
    if index <= 0:
        newNode = ListNode(value)
        newNode.next = head
        return newNode
    
    count = 0
    cur = head

    #iterate until we get to index - 1 or the next property is null
    #meaning we have reached the end of the list
    while count < index - 1 and cur.next is not None:
        count += 1
        cur = cur.next

    #insert our node into our main case
    #make previous node point to new node
    #make new node's next point to cur
    prev = cur
    cur = cur.next
    prev.next = ListNode(value)

    if cur is not None:
        prev.next.next = cur
        # newNode = prev.next
        # newNode.next = cur
    return head