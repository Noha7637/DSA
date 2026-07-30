class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 0
        for j in range(len(word)):
            if j<8:
                count+=1
            elif j<16:
                count+=2
            elif j<24:
                count+=3
            elif j<26:
                count+=4
        return count
                    
        
        





        