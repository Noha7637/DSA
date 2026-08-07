class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        while i<len(nums1):
            if i>=m:
                nums1.pop(i)
            else:
                i+=1
        ptr2=0
        ptr1=0
        while ptr2<len(nums2):
            while ptr1<len(nums1):
                if nums1[ptr1]>nums2[ptr2]:
                    nums1.insert(ptr1, nums2[ptr2])
                    ptr1+=1
                    break
                ptr1+=1
            else:
                nums1.append(nums2[ptr2])
            ptr2+=1


              
            
                
            
        
        
        
        

        





        
        

        