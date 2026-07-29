class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        count = {}
        for i in range(n+1):
            count = Counter(bin(i))
            arr.append(count["1"])
        return arr
        