class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stores (start_index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            # If the current bar is shorter, taller bars
            # cannot extend any farther to the right.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                # The popped rectangle extends from index
                # up to (but not including) current index i.
                width = i - index
                area = height * width
                max_area = max(max_area, area)

                # The current shorter bar can extend back
                # to where the popped taller bar started.
                start = index

            # Store the earliest valid starting position
            # for a rectangle of this height.
            stack.append((start, h))

        # Process rectangles that extend to the end.
        for index, height in stack:
            width = len(heights) - index
            area = height * width
            max_area = max(max_area, area)

        return max_area