class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        list1 = list(columnTitle)
        list1.reverse()
        add = 0
        for i in range(len(list1)):
            add+= 26**i * (ord(list1[i])-64)
        return add


            
