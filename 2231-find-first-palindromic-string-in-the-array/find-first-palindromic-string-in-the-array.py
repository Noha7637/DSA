class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        x = ""
        for word in words:
            if word==word[::-1]:
                x = word
                break
        return x
        
        