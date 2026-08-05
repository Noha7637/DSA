class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = sorted(score, reverse = True)
        j = 0
        for i in range(len(score)):
            j = 0
            while True:
                if score[i] == ranks[j]:
                    if j == 0:
                        score[i] = "Gold Medal"
                    elif j == 1:
                        score[i] = "Silver Medal" 
                    elif j == 2:
                        score[i] = "Bronze Medal"      
                    else:
                        score[i] = str(j+1)   
                    break 
                j += 1
        return score


            
            
            