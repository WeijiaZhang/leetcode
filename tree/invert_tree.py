from __init__ import TreeNode
import Queue

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        que = Queue.Queue()
        if root:
            que.put(root)
        while not que.empty():
            t_node = que.get()
            t_node.left, t_node.right = t_node.right, t_node.left
            if t_node.left:
                que.put(t_node.left)
            if t_node.right:
                que.put(t_node.right)

        return root

    def invert_recur(self, p):
        if p:
            p.left, p.right = p.right, p.left
            self.invert_recur(p.left)
            self.invert_recur(p.right)
