class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        set1 = {"(", "[", "{"}
        set2 = {"]", "}", ")"}
        S = list(s)
        set3 = set(S)
        i = 0
        
        if len(s) % 2 != 0:
            return False
        if set1 >= set3 or set2 >= set3:
            return False
        if len(S) == 2:
            return s in ["()", "[]", "{}"]

        
        while True:
            if len(S) == 0:
                return True
            
            if i >= len(S) - 1:
                return False
                
            if S[i]+S[i+1] == "()" or S[i]+S[i+1] == "[]" or S[i]+S[i+1] == "{}":
                S.pop(i)
                S.pop(i)
                i = 0  
            elif S[i]+S[i+1] in ["(}", "[}", "{]", "(]", "[)", "{)"]:
                return False
            else:
                i += 1  
