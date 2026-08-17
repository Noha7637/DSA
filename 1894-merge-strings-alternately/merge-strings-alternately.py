class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        arr = []
        while i<len(word1) and j<len(word2):
            arr.append(word1[i])
            arr.append(word2[j])
            i+=1
            j+=1
        arr.extend(word1[i:])
        arr.extend(word2[j:])
        return "".join(arr)