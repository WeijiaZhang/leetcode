class solution(object):
    def single_number(self, nums):
        """
        :param nums:
        :return: int
        """
        if len(nums) == 1:
            return nums[0]
        # with extra memory
        # count_dict = {}
        # for i in nums:
        #     if count_dict.get(i, 0) == 0:
        #         count_dict[i] = 1
        #     else:
        #         count_dict[i] += 1
        #
        # for key in count_dict.keys():
        #     if count_dict[key] == 1:
        #         return key

        # without extra memory: bit manipulation: xor all the nums
        single_num = 0
        for i in range(len(nums)):
            single_num ^= nums[i]
        return single_num
