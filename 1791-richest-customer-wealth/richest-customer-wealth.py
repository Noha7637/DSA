class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        x = [sum(wealth) for wealth in accounts]
        return max(x)