class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = list(s)
        for i in range(len(arr)):
            if arr[i].isupper():
                arr[i] = arr[i].lower()
        new_string = "".join(arr)
        return new_string

             
        