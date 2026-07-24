class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        check = False
        if n>0:
            for i in range(21):
                for j in range(21):
                    for k in range(21):
                        if n == (2**i)*(3**j)*(5**k):
                            check = True
                            break
                    if check == True:
                        break
                if check == True:
                    break
        return check
                



                            
                        


        
           