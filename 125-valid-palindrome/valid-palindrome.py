class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = s.lower()
        arr = []
        for i in range(len(k)):
            if k[i].isalpha() or k[i].isdigit():
                arr.append(k[i])
        return arr == arr[::-1]


        