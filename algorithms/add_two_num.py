# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    head = ListNode(-1)
    p = head
    my_sum = 0
    while l1 or l2:
        # do not need carry in this way
        my_sum /= 10
        if l1:
            my_sum += l1.val
            l1 = l1.next
        if l2:
            my_sum += l2.val
            l2 = l2.next
        p.next = ListNode(my_sum % 10)
        p = p.next
    # create extra new node
    if my_sum / 10 == 1:
        p.next = ListNode(1)
    return head.next



