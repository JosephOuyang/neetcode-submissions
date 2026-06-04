class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftHighest, rightHighest = height[left], height[right]
        totalWater = 0
        while left < right:
            if leftHighest < rightHighest:
                left += 1
                leftHighest = max(height[left], leftHighest)
                totalWater += leftHighest - height[left]
            else:
                right -= 1
                rightHighest = max(height[right], rightHighest)
                totalWater += rightHighest - height[right]
        return totalWater

        