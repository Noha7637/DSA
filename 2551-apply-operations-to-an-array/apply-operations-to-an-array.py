class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i], nums[i+1] = nums[i]*2, 0
        j = 0
        while j<len(nums):
            if nums[j]==0:
                arr.append(nums.pop(j))
            else:
                j+=1
        nums.extend(arr)
        return nums