class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
def BinaryTree(values):
    
    if not values:
        return None
        
    tree = Tree(values[0])
    
    for value in values[1:]:
        cur = tree
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = Tree(value)
                    break
                cur = cur.left
            else:
                if cur.right is None:    
                    cur.right = Tree(value)
                    break
                cur = cur.right
    return tree