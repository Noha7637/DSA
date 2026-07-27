class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        counter = 0
        while True:
            for i in range(len(heights)-1):
                if heights[i+1]>heights[i]:
                    heights[i], heights[i+1] = heights[i+1], heights[i]
                    names[i], names[i+1] = names[i+1], names[i]
                    counter = 1
            if counter == 0:
                break
            counter = 0
        return names
            
            


            
        