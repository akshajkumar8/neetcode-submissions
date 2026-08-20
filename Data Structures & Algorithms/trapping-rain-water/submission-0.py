class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        total_water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
            else:
                right -= 1
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
        
        return total_water