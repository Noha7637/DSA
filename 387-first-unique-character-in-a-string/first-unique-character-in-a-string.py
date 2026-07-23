class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = -1
        y = []
        for i in range(len(s)):
            y.append(s[i])

        count = Counter(y)

        for i in range(len(y)):
            if count[y[i]] == 1:
                x = i
                break           
        return x

            

            

                    
            


