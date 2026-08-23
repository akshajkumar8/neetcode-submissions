class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_freq = 0
        best = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(count[s[right]], max_freq)
            
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)
        
        return best
