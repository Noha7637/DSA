class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = list(Counter(nums).items())
        count = list(map(list, count))
        count.sort(key=lambda x: x[1])
        print(count)
        return count[0][0]
        
        
        