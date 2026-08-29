class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while nums!=sorted(nums):
            minsum = nums[0]+nums[1]
            index = 0
            for i in range(1, len(nums)-1):
                temp = nums[i]+nums[i+1]
                if temp<minsum:
                    minsum = temp
                    index = i
            nums.pop(index)
            nums.pop(index)
            nums.insert(index, minsum)
            count+=1
        return count
