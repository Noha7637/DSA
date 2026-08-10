class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_max = 0
        for i in range(len(nums)):
            if i%2==0:
                sum_max += nums[i]
        return sum_max