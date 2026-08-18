class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        arr = []
        finalarr = []
        black = "B"*k
        count = 0
        for i in range(len(blocks)-k+1):
            temp = blocks[i:i+k]
            arr.append(temp)
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j]!=black[j]:
                    count+=1
            finalarr.append(count)
            count = 0
        return min(finalarr)

            
