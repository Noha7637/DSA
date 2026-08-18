class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        arr = []
        diff = 0
        if len(nums)==1:
            return 0
        for i in range(len(nums)-k+1):
           diff = nums[i+k-1]-nums[i]
           arr.append(diff)
        return min(arr)
        
           
           

