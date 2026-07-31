class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set_1 = list(map(str.lower, words))
        arr = []
        for i in range(len(set_1)):
            if set(set_1[i]) <= set("qwertyuiop"):
                arr.append(words[i])
            elif set(set_1[i])<=set("asdfghjkl"):
                arr.append(words[i])
            elif set(set_1[i])<=set("zxcvbnm"):
                arr.append(words[i])
        return arr
            
        
        
                
    
        