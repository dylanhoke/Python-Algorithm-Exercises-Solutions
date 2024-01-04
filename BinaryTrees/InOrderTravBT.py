class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def solution(root):
    result = []
    if root is not None:
        result.extend(solution(root.left))
        
        result.append(root.value)
        
        result.extend(solution(root.right))
        
    return result
        
    
    # result = []
    # queue = [root]
    
    # while queue:
    #     cur = queue.pop(0)
        
    #     if cur.left:
    #         queue.append(cur.left)
    #         continue
        
    #     result.append(cur.value)
        
    #     if cur.right:
    #         queue.append(cur.right)