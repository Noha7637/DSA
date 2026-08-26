class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp = -100000
        first = 0
        second = 0
        summation = 0
        while first<len(nums)-k+1:
            summation += nums[second]
            if second==first+k-1:
                if temp < summation/k:
                    temp = summation/k
                summation-=nums[first]
                first+=1
            second += 1
        return temp
            