class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        half1 = ""
        half2 = ""
        total = ""
        if len(s)%2 == 0:
            half1 = "".join(sorted(s[0:len(s)/2]))
            half2 = half1[::-1]
            total = half1  + half2
        elif len(s)%2 != 0:
            half1 = "".join(sorted(s[0:len(s)//2]))
            half2 = half1[::-1]
            total = half1 + s[len(s)//2] + half2
        return total

        
            
            
            

        





        