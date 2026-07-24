class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        triangle = ""
        sum = 0
        for i in range(3):
            for j in range(3):
                if i!=j:
                    sum = sum + nums[j]
            if nums[i]>=sum:
                triangle = "none"
                break
            sum = 0
        else:
            if nums[0]==nums[1]==nums[2]:
                triangle = "equilateral"
            elif nums[0]!=nums[1] and nums[1]!=nums[2] and nums[0]!=nums[2]:
                triangle = "scalene"
            else: 
                triangle = "isosceles"
                
        return triangle
                
        