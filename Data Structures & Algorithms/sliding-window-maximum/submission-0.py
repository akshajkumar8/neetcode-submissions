from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Stores indices of useful maximum candidates.
        # Their values are maintained in decreasing order.
        q = deque()

        # Store the maximum from each complete window
        result = []

        # Process each number from left to right
        for right in range(len(nums)):

            # Remove indices that are outside the current window
            # The window's left boundary is right - k + 1
            while q and q[0] < right - k + 1:
                q.popleft()

            # Remove smaller or equal values from the back.
            # They cannot be the maximum while the current
            # larger (or equal), newer value is in the window.
            while q and nums[q[-1]] <= nums[right]:
                q.pop()

            # Add the current element's index
            q.append(right)

            # Once we've processed k elements,
            # the window is complete
            if right >= k - 1:

                # The front holds the maximum's index
                result.append(nums[q[0]])

        return result