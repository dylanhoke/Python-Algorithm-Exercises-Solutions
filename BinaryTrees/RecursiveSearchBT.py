class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
def solution(root, value):
    if root is None:
        return False
    if root.value == value:
        return True
    elif root.value < value:
        return solution(root.right, value)
        # cur = cur.right
    else:
        return solution(root.left, value)
        # cur = cur.left