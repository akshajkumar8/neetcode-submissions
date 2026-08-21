class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        two_below = 1
        one_below = 2

        for i in range(3, n + 1):
            current = one_below + two_below
            two_below = one_below
            one_below = current
        
        return current
