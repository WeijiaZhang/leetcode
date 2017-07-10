from __init__ import *

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # keypoint: whether has follow.next = prev
        # one point has one step while another has two steps
        # a node of cycle has no null next

        # faster way by except None
        # try:
        #     slow = head
        #     fast = head.next
        #     while slow is not fast:
        #         slow = slow.next
        #         fast = fast.next.next
        #     return True
        # except:
        #     return False
        if (not head) or (not head.next):
            return False
        prev, follow = head, head.next
        while follow and follow.next:
            prev = prev.next
            follow = follow.next.next
            if prev == follow:
                return True
        return False
