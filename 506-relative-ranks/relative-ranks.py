class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = sorted(score, reverse = True)
        ranks_dict = {ranks[i]: str(i+1) for i in range(len(ranks))}
        ranks_dict[ranks[0]] = "Gold Medal"
        if len(ranks_dict)>1:
            ranks_dict[ranks[1]] = "Silver Medal"
        if len(ranks_dict)>2:
            ranks_dict[ranks[2]] = "Bronze Medal"
        return [ranks_dict[i] for i in score]