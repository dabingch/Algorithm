class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:
            left = height[l]
            right = height[r]
            length = min(left, right)
            width = r - l
            area = length * width
            maxArea = max(maxArea, area)
            if left < right:
                l += 1
            else:
                r -= 1
        
        return maxArea