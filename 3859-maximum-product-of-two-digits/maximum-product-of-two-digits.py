class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = []
        new_n = str(n)
        for i in range(len(new_n)):
            for j in range(len(new_n)):
                if i!=j:
                    arr.append(int(new_n[i]) * int(new_n[j]))
        return max(arr)
                    
                

        