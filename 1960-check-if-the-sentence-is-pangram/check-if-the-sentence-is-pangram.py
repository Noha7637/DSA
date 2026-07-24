class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        arr_sentence = [i for i in sentence]
        new_sentence = set(arr_sentence)
        if len(new_sentence) == 26:
            return True
        else:
            return False
        
        
    
            


        