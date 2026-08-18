class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        i = 0
        j = 0
        while i<len(a):
            if a[i]=="#":
                if i == 0:
                    a.pop(i)
                elif i>0:
                    a.pop(i)
                    a.pop(i-1)
                    i = i-1
            else:
                i+=1
        while j<len(b):
            if b[j]=="#":
                if j == 0:
                    b.pop(j)
                elif j > 0:
                    b.pop(j)
                    b.pop(j-1)
                    j = j-1
            else:
                j+=1
        if a == b:
            return True
        else:
            return False
        