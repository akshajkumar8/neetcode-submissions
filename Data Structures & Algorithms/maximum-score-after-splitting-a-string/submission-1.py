class Solution:
    def maxScore(self, s: str) -> int:
        num_ones = s.count('1')
        zeros = 0
        max_score = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            else:
                num_ones -= 1
            max_score = max(max_score, num_ones + zeros)
        return max_score