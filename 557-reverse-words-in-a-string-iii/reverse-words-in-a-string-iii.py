class Solution:
    def reverseWords(self, s: str) -> str:
        arr1 = s.split()
        arr2 = []
        for i in range(len(arr1)):
            arr2.append(arr1[i][::-1])
        return " ".join(arr2)