class Tree(object):
    def __int__(self, x):
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
           
    cur = Tree(value)

    if value < branch.value:
        branch.left = cur
    else:
        branch.right = cur


    # if value < root.value:
    #     root.left = solution(root.left, value)
    # else:
    #     root.right = solution(root.right,value)
    
    return root