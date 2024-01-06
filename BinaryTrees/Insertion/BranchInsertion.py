class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def solution(root:Tree, value:int) -> Tree:
    if root is None:
        return Tree(value)
    
    cur = root
    branch = None

    while cur:
        branch = cur
        if value < cur.value:
            cur = cur.left
        else:
           cur =  cur.right
           
    new_node = Tree(value)

    if value < branch.value:
        branch.left = new_node
    else:
        branch.right = new_node


    # if value < root.value:
    #     root.left = solution(root.left, value)
    # else:
    #     root.right = solution(root.right,value)
    
    return root