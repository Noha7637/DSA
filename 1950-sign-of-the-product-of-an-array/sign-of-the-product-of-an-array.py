class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0 
        for i in range(len(nums)):
            if i==0:
                x = nums[i]
            else:
                x = x * nums[i]
        if x<0:
            return -1
        elif x==0:
            return 0
        elif x>0:
            return 1
        

        