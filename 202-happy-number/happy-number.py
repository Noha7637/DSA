class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        check = False
        sum = 0
        y = str(n)
        count = 0
        while True:
            if count == 1000:
                break
            for i in range(len(y)):
                sum = sum + (n%10)**2
                n = n//10
            n = sum
            if n==1:
               check = True
               break
            sum = 0
            count = count + 1
            y = str(n)
        return check
            
                

        