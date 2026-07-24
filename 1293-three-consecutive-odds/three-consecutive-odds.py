class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3:
            return False
        else:
            for i in range(len(arr)):
                if i<len(arr)-2:
                    if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
                        return True
                        break
            else:
                return False
    