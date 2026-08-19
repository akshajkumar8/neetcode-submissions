from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        lucky = -1
        for num in count:
            if num == count[num]:
                lucky = max(num, lucky)
        return lucky
            