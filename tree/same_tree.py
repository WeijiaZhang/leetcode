from symmetric_tree import *

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.is_same_recur(p,q)


    def is_same_recur(self, p, q):
        if (not  p) or (not q):
            return  p == q
        if p.val != q.val:
            return False
        return  self.is_same_recur(p.left, q.left) and self.is_same_recur(p.right, q.right)
