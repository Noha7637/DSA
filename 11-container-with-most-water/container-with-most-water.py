class Solution:
    def maxArea(self, height: List[int]) -> int:
        arr = []
        ptr1 = 0
        ptr2 = len(height) - 1
        for i in range(len(height)):
            arr.append(min(height[ptr1], height[ptr2])*(abs(ptr2-ptr1)))
            if height[ptr1] > height[ptr2]:
                ptr2-=1
            elif height[ptr2] > height[ptr1]:
                ptr1+=1
            elif height[ptr2] == height[ptr1]:
                ptr1+=1
        return max(arr)