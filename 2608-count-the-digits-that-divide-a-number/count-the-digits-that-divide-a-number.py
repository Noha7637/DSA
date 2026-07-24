class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = num
        y = str(num)
        count = 0
        for i in range(len(y)):
            if num%(n%10)==0:
                count+=1
            n = n//10
        return count
        