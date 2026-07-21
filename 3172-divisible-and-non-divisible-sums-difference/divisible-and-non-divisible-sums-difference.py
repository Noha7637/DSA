class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        group_1 = 0
        group_2 = 0
        for i in range(1,n+1):
            if i%m == 0:
                group_1= group_1 + i
            else:
                group_2 = group_2 + i
        return group_2 - group_1
            
        