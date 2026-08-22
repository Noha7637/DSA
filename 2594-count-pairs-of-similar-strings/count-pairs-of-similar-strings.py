class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            temp = list(set(words[i]))
            temp.sort()
            words[i]= "".join(temp)
        for j in range(len(words)):
            for k in range(len(words)):
                if k>j:
                    if words[j]==words[k]:
                        count+=1
        return count

        