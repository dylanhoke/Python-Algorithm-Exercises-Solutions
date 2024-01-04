class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root):
    
    result = []
    
    if root is not None:
        
        solution(root.left)
        
        solution(root.right)
        
        root.left, root.right = root.right, root.left
    
    return root