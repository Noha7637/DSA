class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod = 0
        for i in range(len(str(n))):
            if i == 0:
                prod = int(str(n)[i])
            else:
                prod = prod * int(str(n)[i])

        return prod - sum([int(i) for i in str(n)])
                
            
        