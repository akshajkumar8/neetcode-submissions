from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Count how many of each character we need
        need = Counter(t)

        # Track character frequencies in the current window
        window = defaultdict(int)

        # Number of distinct character requirements to satisfy
        required = len(need)

        # Number of requirements currently satisfied
        formed = 0

        # Left boundary of our sliding window
        left = 0

        # Track the smallest valid window found
        min_length = float("inf")
        min_start = 0

        # Expand the window by moving right
        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            # Did this character just reach its required count?
            if char in need and window[char] == need[char]:
                formed += 1

            # Shrink while the window contains everything needed
            while formed == required:
                # Calculate the current window length
                window_length = right - left + 1

                # Save the smallest valid window
                if window_length < min_length:
                    min_length = window_length
                    min_start = left

                # Remove the leftmost character
                left_char = s[left]
                window[left_char] -= 1

                # Did removing it break a requirement?
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                # Move the left boundary forward
                left += 1

        # No valid substring was found
        if min_length == float("inf"):
            return ""

        # Return the shortest valid substring
        return s[min_start:min_start + min_length]