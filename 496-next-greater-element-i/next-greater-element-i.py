class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ptr1 = 0
        indx = 0
        arr = []
        while ptr1 < len(nums1):
            indx = nums2.index(nums1[ptr1])
            if indx == len(nums2)-1:
                arr.append(-1)
            else:
                for i in range(indx+1, len(nums2)):
                    if nums2[i]>nums2[indx]:
                        arr.append(nums2[i])
                        break
                else:
                    arr.append(-1)
            ptr1+=1
        return arr   
    
