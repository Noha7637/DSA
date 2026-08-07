class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = []
        ptr = 0
        while ptr<len(nums):
            if nums[ptr]==0:
                nums.pop(ptr)
                m.append(0)
            else:
                ptr+=1
        for i in range(len(m)):
            nums.append(0)
        


        