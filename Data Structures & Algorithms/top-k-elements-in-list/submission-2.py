from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]  # Create n+1 independent empty lists, one for each possible frequency from 0 to n

        for num, count in freq.items():
            buckets[count].append(num)  # Put the number into the bucket whose index equals its frequency

        result = []

        for count in range(len(buckets) - 1, 0, -1):  # Visit frequency buckets from highest to lowest, skipping frequency 0
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result