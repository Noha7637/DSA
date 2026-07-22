class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniform_case = s.lower()
        new_uniform_case = uniform_case
        counter = 0
        for i in range(len(new_uniform_case)-1):
            if new_uniform_case[i] != new_uniform_case[i+1]:
                counter = counter + 1
        return counter
            
            


        