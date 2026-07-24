class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        arr_sentence = [i for i in sentence]
        new_sentence = list(sorted(set(arr_sentence)))
        alphabet = [chr(i).lower() for i in range(65,91)]
        if alphabet == new_sentence:
            return True
        else:
            return False
        
        
    
            


        