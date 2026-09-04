class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for i in range(1, len(word)):
            if word[i]==word[i].upper():
                count += 1
        if word[0]==word[0].upper():
            if count==0 or count==len(word)-1:
                return True
            elif count>0 and count<len(word)-1:
                return False
        else:
            if count==0:
                return True
            else:
                return False