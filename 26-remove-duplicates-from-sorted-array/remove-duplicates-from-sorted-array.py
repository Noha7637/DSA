class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0
        count = 0
        for ptr2 in range(1, len(nums)):
            if nums[ptr1]<nums[ptr2]:
                nums[ptr1+1], nums[ptr2] = nums[ptr2], nums[ptr1+1]
                ptr1+=1
        return len(nums[0:ptr1+1])
       
            
        
            
            

        