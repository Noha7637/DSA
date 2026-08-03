class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0
        ptr2 = 1
        while ptr1<len(nums)-1:
            if ptr2==len(nums)-1:
                if nums[ptr1]==nums[ptr2]:
                    nums.pop(ptr2)
                ptr1 +=1
                ptr2 = ptr1 + 1
            elif nums[ptr2]==nums[ptr1]:
                nums.pop(ptr2)
            else:
                ptr2+=1
        return len(nums)
            
        
            
            

        