class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        category_1 = []
        category_2 = []
        Winner = []
        Loser = []

        # grouping in to two winner and loser lists
        for i in matches:
            Winner.append(i[0])
            Loser.append(i[1])

        # checking for the answer[0] items
        category_1 = list(set(Winner)-set(Loser))

        # checking for the answer[1] items
        count = Counter(Loser)
        for i,j in count.items():
            if j == 1:
                category_2.append(i)
            
        output = [sorted(set(category_1)), sorted(set(category_2))]
        return output

                    
            
                    
            
        
            

            
            

        