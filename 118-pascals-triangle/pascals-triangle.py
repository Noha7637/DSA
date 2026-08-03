class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        arrout = []
        for i in range(numRows):
            if i==0:
                arrout.append([1])
            elif i==1:
                arrout.append([1,1])
            else:
                for j in range(i+1):
                    if j == 0 or j == i:
                        arr.append(1)
                    else:
                        arr.append(arrout[i-1][j-1] + arrout[i-1][j])
                arrout.append(arr)
                arr = []
        return arrout

                    
                        


                
                
            
        