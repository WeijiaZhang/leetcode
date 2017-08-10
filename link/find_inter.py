from __init__ import *

class Solution(object):
    def getIntersectionNode(self, head1, head2):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # if we connect on link head with tail
        # that problem is changed to how to find cycle in linklist
        if self.is_intersection(head1, head2):
            p1, p2 = head1, head2
            len1, len2 = 0, 0
            while p1 is not None:
                len1 += 1
                p1 = p1.next
            while p2 is not None:
                len2 += 1
                p2 = p2.next
            if len1 > len2:
                p_long, p_short = head1, head2
            else:
                p_long, p_short = head2, head1
            # node of long list should take more steps of 'diff length'
            for i in range(0, abs(len1 - len2)):
                p_long = p_long.next
            # after we believe that two link list has intersection
            # there is no need to detect whether node is null
            while p_long != p_short and p_long is not None and p_short is not None:
                p_long = p_long.next
                p_short = p_short.next
            return p_long

        # popular solution
        p1, p2 = head1, head2
        while p1 is not p2:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            p1 = p1.next if p1 is not None else head2
            p2 = p2.next if p2 is not None else head1
        # only 2 ways to get out of the loop, they meet or the both hit the end=None
        return p1

    # however we also can find intersection node
    # by calculate 'diff length' between two linklist
    def is_intersection(self, p1, p2):
        if p1 is None or p2 is None:
            return False
        while p1.next is not None:
            p1 = p1.next
        while p2.next is not None:
            p2 = p2.next
        return p1 == p2
