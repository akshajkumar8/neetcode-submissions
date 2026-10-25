class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # A permutation of s1 cannot fit inside a shorter string
        if len(s1) > len(s2):
            return False

        # Each index represents a lowercase letter:
        # 0 = a, 1 = b, ..., 25 = z
        s1_count = [0] * 26
        window_count = [0] * 26

        # Count characters in s1 and the first window of s2
        for i in range(len(s1)):
            s1_index = ord(s1[i]) - ord("a")
            window_index = ord(s2[i]) - ord("a")

            s1_count[s1_index] += 1
            window_count[window_index] += 1

        # Check whether the first window is a permutation
        if s1_count == window_count:
            return True

        # Slide the window across the rest of s2
        for right in range(len(s1), len(s2)):
            # Add the new character entering from the right
            new_index = ord(s2[right]) - ord("a")
            window_count[new_index] += 1

            # Remove the character leaving from the left
            left = right - len(s1)
            old_index = ord(s2[left]) - ord("a")
            window_count[old_index] -= 1

            # Matching frequencies means we found a permutation
            if s1_count == window_count:
                return True

        # No matching window was found
        return False