class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        dictionary = {}
        for i in range(len(code)):
            dictionary[alphabet[i]]=code[i]
        arr = []
        temp = ""
        for i in range(len(words)):
            for j in range(len(words[i])):
                temp+=dictionary[words[i][j]]
            arr.append(temp)
            temp = ""
        return len(set(arr))



        