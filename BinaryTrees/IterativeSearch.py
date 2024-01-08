class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root, value):
    
    if root is None:
        return False
    
    cur = root
    
    while cur:
        if value == cur.value:
            return True
        
        if value < cur.value:
            cur = cur.left
        else:
            cur = cur.right
    return False
