class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root):
    
    result = []
    
    if root is not None:
        
        left_subtree = solution(root.left)
        
        right_subtree = solution(root.right)
        
        root.left, root.right = right_subtree.right, left_subtree.left
    
    return root