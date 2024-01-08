class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root):
    if root is not None:
        root.left, root.right = root.right, root.left
        solution(root.left)
        solution(root.right)
    return root