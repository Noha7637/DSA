class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr1 = []
        arr2 = []
        for i in range(rowIndex + 1):
            if i == 0:
                arr1.append([1])
            elif i == 1:
                arr1.append([1, 1])
            else:
                arr2 = [1,1]
                for j in range(len(arr1[i-1])-1):
                    arr2.insert(j+1, arr1[i-1][j] + arr1[i-1][j+1])
                arr1.append(arr2)
        return arr1[len(arr1)-1]
