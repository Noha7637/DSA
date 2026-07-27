class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        dictionary = {heights[i]:names[i] for i in range(len(names))}
        counter = 0
        while True:
            for i in range(len(heights)-1):
                if heights[i+1]>heights[i]:
                    heights[i], heights[i+1] = heights[i+1], heights[i]
                    counter += 1
            if counter == 0:
                break
            counter = 0
        arr = [dictionary[i] for i in heights]
        return arr
            
            


            
        