class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        new_sentence = set(list(sentence))
        if len(new_sentence) == 26:
            return True
        else:
            return False
        
        
    
            


        