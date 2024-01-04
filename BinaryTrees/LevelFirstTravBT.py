class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
    
def solution(root):
    """
    Perform a level first traversal of the given binary tree
    
    the output should be an integer array consisting of all the node values
    in the level first traversal order
    
    when enqueueing, enqueue the left then enqueue the right
    
    for the queue implementation you can make your own linked list or you can
    us something built in as a queue even if it has poor time complexity
    """
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