class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def solution(root, value):

    if root is None:
        return False
    
    #make reference to node
    cur = root

    #as long as it exists
    while cur:

        if value == cur.value:
            return True
        
        if value < cur.value: # was root.value
            # return solution(root.left, value)
            cur = cur.left
        elif value > cur.value: # was root.value
            # return solution(root.right,value)
            cur = cur.right
    return False 