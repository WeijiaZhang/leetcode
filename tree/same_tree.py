from symmetric_tree import *

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # return self.is_same_recur(p,q)
        queue1, queue2 = Queue.Queue(), Queue.Queue()
        queue1.put(p)
        queue2.put(q)
        while (not  queue1.empty()) and (not queue2.empty()):
            p_t, q_t = queue1.get(), queue2.get()
            if (not p_t) and (not q_t):
                continue
            elif (not p_t) or (not q_t):
                return False
            elif p_t.val != q_t.val:
                return False
            queue1.put(p_t.left)
            queue1.put(p_t.right)
            queue2.put(q_t.left)
            queue2.put(q_t.right)
        return True


    def is_same_recur(self, p, q):
        if (not  p) or (not q):
            return  p == q
        if p.val != q.val:
            return False
        return  self.is_same_recur(p.left, q.left) and self.is_same_recur(p.right, q.right)
