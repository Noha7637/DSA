class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = list(map(str,nums))
        str_nums = "".join(new_nums)
        digit_sum = sum([int(i) for i in str_nums])
        element_sum = sum(nums)
        return abs(element_sum - digit_sum)

        