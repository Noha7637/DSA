class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        arr = []
        for i in address:
            if i == ".":
                arr.append("[.]")
            else:
                arr.append(i)
        return "".join(arr)
            
        