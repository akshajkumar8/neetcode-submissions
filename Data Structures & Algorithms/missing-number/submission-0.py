class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        for i in range(len(nums) + 1):
            if i not in seen:
                return i
        # Time: O(n), Space: O(n)
        # XOR alternative: O(n) time, O(1) space