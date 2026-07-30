class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        set1 = list(set(word))
        count = 0
        for i in range(len(word)):
            for j in range(len(set1)):
                if word[i] == set1[j]:
                    if j<8:
                        count+=1
                    elif j<16:
                        count+=2
                    elif j<24:
                        count+=3
                    elif j<26:
                        count+=4
        return count
                    
        
        





        