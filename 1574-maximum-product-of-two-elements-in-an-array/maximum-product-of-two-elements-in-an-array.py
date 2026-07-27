class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        arr_rev = nums[::-1]
        return ((arr_rev[0]-1) * (arr_rev[1]-1))

        