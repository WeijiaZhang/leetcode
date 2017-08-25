class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # because major elemnt appears more than n/2 times
        # so that must sub_array whose xor is 0
        major, count = nums[0], 1
        for num in nums[1:]:
            if count == 0:
                major = num
                count = 1
            elif major == num:
                count += 1
            else:
                count -= 1
        return major
