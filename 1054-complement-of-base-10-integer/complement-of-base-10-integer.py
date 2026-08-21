class Solution:
    def bitwiseComplement(self, n: int) -> int:
        number = bin(n)[2:]
        complement = []
        for i in range(len(number)):
            if number[i]=="0":
                complement.append(1)
            elif number[i]=="1":
                complement.append(0)
        complement.reverse()
        total = 0
        for i in range(len(complement)):
            total+= complement[i] * 2**i
        return total