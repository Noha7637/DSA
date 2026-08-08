class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        temporary = len(digits)-1
        for i in range(len(digits)):
            number += digits[i]*10**temporary
            temporary -= 1
        number+=1
        temporary = len(str(number))-1
        arr = []
        for i in range(len(str(number))):
           arr.append(number//10**temporary)
           number = number%10**temporary
           temporary-=1
        return arr
            