class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high) // 2
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
            if total_hours > h:
                low = mid + 1
            else:
                high = mid
        return low

    # import math
    # total_hours += math.ceil(pile / mid)