from algorithms.add_two_num import addTwoNumbers
from algorithms.add_two_num import ListNode
from algorithms.permutations import permute


def list2linklist(arr):
    head = ListNode(-1)
    p = head
    for val in arr:
        new_node = ListNode(val)
        p.next = new_node
        p = new_node
    return head.next


def print_linklist(p):
    while p != None:
        print(p.val)
        p = p.next


def main():
    # arr1 = [3, 4, 5]
    # arr2 = [2, 4, 6]
    # l1 = list2linklist(arr1)
    # l2 = list2linklist(arr2)
    # print_linklist(addTwoNumbers(l1, l2))
    print(permute([1, 2, 3]))

if __name__ == '__main__':
    main()

