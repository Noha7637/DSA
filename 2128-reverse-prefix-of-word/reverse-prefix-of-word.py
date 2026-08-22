class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = list(word)
        arrtemp = []
        temp = 0
        for i in range(len(arr)):
            if arr[i]==ch:
                if i == len(arr)-1:
                    return "".join(arr[::-1])
                else:
                    temp = i
                    arrtemp = arr[0:i+1] 
                    break  
        else:
            return word
        arrtemp.reverse()
        j = temp+1
        while j>=temp+1 and j<len(arr):
            arrtemp.append(arr[j])
            j+=1
        return "".join(arrtemp)
        
