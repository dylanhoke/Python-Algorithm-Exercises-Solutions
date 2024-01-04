# Singly-linked lists are already defined with this interface:

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None


class ListStack:

    def __init__(self):
        self.head = None

    # def tail(self, head):

    #     self.tail = head

    #     while head is not None:
    #         self.tail = self.tail.next
    #     return self.tail

    def enqueue(self, value): #adds to the end of the list

        n = ListNode(value) #creates new node
        
        if not self.head:
            self.head = n
        else:
            current = self.head
            
            while current.next:
                current = current.next
            current.next = n

    def dequeue(self): #remove and discards the first node from the list
        
        if not self.head:
            return None
        else:
            o = self.head.value

            self.head = self.head.next
            
            return o

def LinkListed(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

def solution(ops):

    stack = ListStack()

    for op in ops:

        if op.startswith('e'):

            _, num = op.split()

            value = int(num)

            stack.enqueue(value)

        elif op.startswith('d'):

            stack.dequeue()

    return LinkListed(stack.head)

    # while current is not None:
    #     if 'e' in current.value:
    #         number  = current.value.split()
    #         current.next = number.isdigit()
    #         current = current.next
    #         print(numbers)
