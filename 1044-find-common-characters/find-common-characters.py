class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word1 = words[0]
        arr = []
        for k in range(len(words)):
            words[k] = list(words[k])
        for i in range(len(word1)):
            for j in range(1, len(words)):
                if word1[i] in words[j]:
                    words[j].pop(words[j].index(word1[i]))
                else:
                    break
            else:
                arr.append(word1[i])
        return arr
                
            
                        
                
        
        
        