class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        y = 2 * len(nums)
        for i in range(y):
            if len(ans) < len(nums):
                ans.append(nums[i])
            else:
                ans.append(nums[i-len(nums)])
        return ans
            

        