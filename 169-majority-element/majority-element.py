class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        for i in count.keys():
            if count[i] > len(nums)//2:
                return i 
                break
        