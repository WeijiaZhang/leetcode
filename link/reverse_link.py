from __init__ import ListNode


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverse_recur(self, p, prev=None):
        if not p:
            return prev
        follow = p.next
        p.next = prev
        self.reverse_recur(follow, p)

    def reverse_recur_1(self, head):
        if not head or not head.next:
            return head
        # reverse following node after head
        new_head = self.reverse_recur_1(head.next)
        # then reverse head
        head.next.next = head
        head.next = None
        return new_head
