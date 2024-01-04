# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root:Tree, value:int):
    
    if root is None:
        return Tree(value)
        
    cur = root
    Branch = None # the before reference
    
    while cur: # reference loop
        Branch = cur
        if value > cur.value:
            cur = cur.right
        else:
            cur = cur.left
        
    cur = Tree(value) # assignment  
    
    if value > Branch.value: # the reference assignment
        Branch.right = cur
    else:
        Branch.left = cur
    
    return root