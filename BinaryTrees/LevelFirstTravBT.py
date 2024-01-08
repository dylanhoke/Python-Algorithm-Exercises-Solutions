class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
    
def solution(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        cur = queue.pop(0)
        result.append(cur.value)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return result