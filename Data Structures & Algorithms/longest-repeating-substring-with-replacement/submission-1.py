from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = defaultdict(int)
        max_freq = 0
        longest = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest