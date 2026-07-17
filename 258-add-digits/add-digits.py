class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            x = 0
        else: 
            y = str(num)
            x=0
            while x == 0 or x>=10:
                x=0
                for i in y:
                    x = x + int(i)
                y = str(x)      
        return x
        