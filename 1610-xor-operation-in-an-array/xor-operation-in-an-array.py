class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        """ nums = [start + 2*i for i in range(n)]
        xor = 0
        for j in range(len(nums)):
            if j == 0:
                xor = nums[j]  
            else:
                xor = xor ^ nums[j]  
        return xor """
        nums = [start + 2*i for i in range(n)]
        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor



        