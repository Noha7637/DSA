class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = []
        temp = ""
        for i in range(len(s)):
            if s[i]==" ":
                if " " not in temp and len(temp)>=1:
                    arr.append(temp)
                temp = ""
            else:
                temp+=s[i]
        if temp!="":
            arr.append(temp)
        return len(arr[-1])
            
        