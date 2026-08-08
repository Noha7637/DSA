class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = [] 
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    if j == len(nums2)-1:
                        arr.append(-1)
                        break
                    elif nums2[j+1]>nums2[j]:
                        arr.append(nums2[j+1])
                        break
                    else:
                        for k in range(j+1, len(nums2)):
                            if nums2[k]>nums2[j]:
                                arr.append(nums2[k])
                                break
                        else:
                            arr.append(-1)

        return arr
