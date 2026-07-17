class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        y = str(num)
        x = 0
        if num == 0:
            pass
        else: 
            while x == 0 or x>=10:
                x=0
                for i in y:
                    x = x + int(i)
                y = str(x)      
        return x
        