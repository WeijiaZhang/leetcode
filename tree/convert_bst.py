from __init__ import TreeNode


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) <= 0:
            return None
        root = self.convert_bst(0, len(nums)-1, nums)
        return root

    def convert_bst(self, low, high, nums):
        if low <= high:
            mid = low + (high - low) / 2
            p = TreeNode(nums[mid])
            p.left = self.convert_bst(low, mid-1, nums)
            p.right = self.convert_bst(mid+1, high, nums)
            return p
        return None
