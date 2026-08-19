class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while True:
            if n==0:
                return False
            if n==1:
                return True
            n = n/2
            if n%1!=0:
                return False
            
        
