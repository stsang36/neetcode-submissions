class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        n = len(heights)
        left = 0
        right = n - 1

        maxArea = 0

        while left < right:
            if heights[left] < heights[right]:
                s = heights[left] * (right - left)
                left += 1
            else:
                s = heights[right] * (right - left)
                right -= 1

            maxArea = max(maxArea, s)

        return maxArea     


        
        