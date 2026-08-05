class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = sorted(score, reverse = True)
        idx = 0
        for i in range(len(ranks)):
            idx = score.index(ranks[i])
            if i == 0:
                score[idx]= "Gold Medal"
            elif i==1:
                score[idx]= "Silver Medal"
            elif i==2:
                score[idx]= "Bronze Medal"
            else:
                score[idx]= str(i+1)
        return score
                
        