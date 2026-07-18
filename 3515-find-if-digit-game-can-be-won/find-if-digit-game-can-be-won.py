class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        y = True
        a = 0
        b = 0
        for i in nums:
            x = str(i)
            if len(x) == 1:
                a = a + int(x)
            else:
                b = b + int(x)
        if a > b:
            pass
        else:
            a = 0
            b = 0
            for i in nums:
                x = str(i)
                if len(x) == 2:
                    a = a + int(x)
                else:
                    b = b + int(x)
            if b >= a:
                y = False
            else:
                y = True
        return y