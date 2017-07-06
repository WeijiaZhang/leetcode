from symmetric_tree import *

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.max_depth_recur(root)

    def max_depth_recur(self, p):
        if not p:
            return 0
        d_left = self.max_depth_recur(p.left)
        d_right = self.max_depth_recur(p.right)
        return max(d_left, d_right)+1
