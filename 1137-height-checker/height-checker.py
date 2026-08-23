class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        total = 0
        for i in range(len(heights)):
            if sorted_height[i]!=heights[i]:
                total+=1
        return total