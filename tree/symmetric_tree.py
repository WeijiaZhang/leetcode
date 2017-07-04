import Queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SymetricTree(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # return root == None or self.is_symetric_recur(root.left, root.right)
        if not root:
            return True
        q_left, q_right = Queue.Queue(), Queue.Queue()
        q_left.put(root.left)
        q_right.put(root.right)
        while((not q_left.empty()) and (not q_right.empty())):
            t_left = q_left.get()
            t_right = q_right.get()
            if t_left == None and t_right == None:
                continue
            elif t_left == None or t_right == None:
                return False
            elif t_left.val != t_right.val:
                return False
            q_left.put(t_left.left)
            q_right.put(t_right.right)
            q_left.put(t_left.right)
            q_right.put(t_right.left)
        return True



    def is_symetric_recur(self, t_left, t_right):
        if (t_left == None or t_right == None):
            return t_left == t_right
        if (t_left.val != t_right.val):
            return False
        return self.is_symetric_recur(t_left.left, t_right.right)\
            and self.is_symetric_recur(t_left.right, t_right.left)

