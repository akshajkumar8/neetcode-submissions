class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_s = {}
        seen_t = {}
        for char in s:
            if char in seen_s:
                seen_s[char] += 1
            else:
                seen_s[char] = 1
        for char in t:
            if char in seen_t:
                seen_t[char] += 1
            else:
                seen_t[char] = 1
        return seen_s == seen_t
                
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        for c in counts:
            if c != 0:
                return False
        return True
"""
        
        
        