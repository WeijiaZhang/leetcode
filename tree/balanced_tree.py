from __init__ import *


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs_height(root) != -1

    # top down approach: find depth of current node
    def is_balanced_recur(self, p):
        if not p:
            return True
        d_left = self.depth(p.left)
        d_right = self.depth(p.right)
        return abs(d_left - d_right) <= 1 and self.is_balanced_recur(p.left) and self.is_balanced_recur(p.right)

    def depth(self, p):
        if not p:
            return 0
        d_left = self.depth(p.left)
        d_right = self.depth(p.right)
        return max(d_left, d_right)+1

    # bottom-up approach:return -1 when subtree is not balanced recursively
    def dfs_height(self, p):
        if not p:
            return 0
        d_left = self.dfs_height(p.left)
        if d_left == -1:
            return -1
        d_right = self.dfs_height(p.right)
        if d_right == -1:
            return -1
        if abs(d_left - d_right) > 1:
            return -1
        return max(d_left, d_right) + 1
