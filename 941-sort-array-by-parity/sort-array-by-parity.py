class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        temp1 = []
        temp2 = []
        for i in range(len(nums)):
            if nums[i]%2!=0:
                temp2.append(nums[i])
            elif nums[i]%2==0:
                temp1.append(nums[i])
        return temp1 + temp2
        
            