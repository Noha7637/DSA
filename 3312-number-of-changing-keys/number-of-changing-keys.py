class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniform_case = s.lower()
        counter = 0
        for i in range(len(uniform_case)-1):
            if uniform_case[i] != uniform_case[i+1]:
                counter = counter + 1
        return counter
            
            


        