class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [i**2 for i in nums]
        arr.sort()
        return arr
        