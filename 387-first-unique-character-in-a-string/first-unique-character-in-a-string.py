class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = -1
        count = Counter(s)

        for i in range(len(s)):
            if count[s[i]] == 1:
                x = i
                break           
        return x

            

            

                    
            


