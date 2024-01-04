class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def solution(requests):
    left = Stack()
    right = Stack()

    def insert(x):

        right = left.push(x)
        
    def remove():
        
        if right.isEmpty():
            while not left.isEmpty():
                right.push(left.pop())
        return right.pop()
        
    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans