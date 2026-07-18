class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        x=len(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                x = i
                break
        return x       
            
            
            
        