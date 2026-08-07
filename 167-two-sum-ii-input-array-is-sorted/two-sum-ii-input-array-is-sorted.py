class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(numbers)-1
        while ptr2>ptr1:
            if target == numbers[ptr1]+numbers[ptr2]:
                return [ptr1+1, ptr2+1]
            elif target > numbers[ptr1]+numbers[ptr2]:
                ptr1+=1
            elif target < numbers[ptr1]+numbers[ptr2]:
                ptr2-=1
        


           