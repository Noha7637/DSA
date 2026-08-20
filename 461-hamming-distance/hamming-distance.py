class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        arr1 = []
        arr2 = []
        bigger  = max(x,y)
        smaller = min(x,y)
        while bigger!=0:
            arr1.append(bigger%2)
            arr2.append(smaller%2)
            bigger//=2
            smaller//=2
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        xor = 0
        count = 0
        for i in range(len(arr2)):
            xor = arr1[i]^arr2[i]
            if xor == 1:
                count+=1
        return count


            
                



        