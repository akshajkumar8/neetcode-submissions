class Solution:
    def countBits(self, n: int) -> List[int]:
        # Create a list filled with 0s of size (n + 1)
        dp = [0] * (n + 1)
        # Loop through every number from 1 to n
        for i in range(1, n + 1):
            # Look up the half of the number and add 1 if current number is odd
            # An even number has the same number of 1s as its half (i >> 1 is i // 2)
            # An odd number has one extra 1 at the end (i & 1 yields 1 if odd, 0 if even)
            dp[i] = dp[i >> 1] + (i & 1)
        return dp