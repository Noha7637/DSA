class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        sent_arr = set(list(sentence))
        return len(sent_arr) == 26
            
        
    
            


        