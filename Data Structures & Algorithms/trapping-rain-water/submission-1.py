class Solution:
    def trap(self, height: List[int]) -> int:
        # Start two pointers at opposite ends of the array
        left = 0
        right = len(height) - 1

        # Track the tallest bar we've seen from each side
        left_max = 0
        right_max = 0

        # Total amount of trapped rainwater
        water = 0

        # Continue until the two pointers meet
        while left < right:

            # Process the side with the shorter current bar
            if height[left] < height[right]:

                # Update the tallest bar seen from the left
                left_max = max(left_max, height[left])

                # Water above this bar = left boundary - bar height
                water += left_max - height[left]

                # Move the left pointer inward
                left += 1

            else:
                # Update the tallest bar seen from the right
                right_max = max(right_max, height[right])

                # Water above this bar = right boundary - bar height
                water += right_max - height[right]

                # Move the right pointer inward
                right -= 1

        # Return the total accumulated water
        return water