class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        m = set(nums2)
        for i in range(len(nums1)):
            if nums1[i] in m:
                return nums1[i]
        else:
            return -1

        