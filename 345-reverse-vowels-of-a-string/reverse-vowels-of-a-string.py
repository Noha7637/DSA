class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        arr = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        arr1 = []
        for i in range(len(lst)):
            if lst[i] in arr:
                arr1.append(lst[i])
                lst[i] = 1
        count = 0
        arr1.reverse()
        for i in range(len(lst)):
            if lst[i]==1:
                lst[i]=arr1[count]
                count+=1
        return "".join(lst)
                