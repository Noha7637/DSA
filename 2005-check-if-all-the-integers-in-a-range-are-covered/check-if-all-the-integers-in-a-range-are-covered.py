class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        result = True
        arr = []
        for RANGE in ranges:
            for i in range(RANGE[0], RANGE[1]+1):
                arr.append(i)
        new_arr = sorted(arr)
        checked_arr = []
        for j in range(left, right + 1):
            checked_arr.append(j)
        common_list = list(set(new_arr) & set(checked_arr))
        common_list.sort()
        if common_list == checked_arr:
            pass
        else:
            result = False
        return result   
        