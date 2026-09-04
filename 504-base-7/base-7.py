class Solution:
    def convertToBase7(self, num: int) -> str:
        arr = []
        temp = abs(num)
        while temp>=7:
            arr.append(temp%7)
            temp = temp//7
        arr.append(temp)
        arr.reverse()
        if num<0:
            arr.insert(0, "-")
            return "".join(map(str, arr))
        else:
            return "".join(map(str, arr))
            

            
        