class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        y = True
        for i in range(len(matrix)):
            if y==False:
                break
            if i>0:
                x = matrix[i]
                z = matrix[i-1]
                for j in range(len(matrix[i])):
                    if j>0:
                        if x[j] == z[j-1]:
                            pass
                        else:
                            y = False
                            break
        return y
             
                

        