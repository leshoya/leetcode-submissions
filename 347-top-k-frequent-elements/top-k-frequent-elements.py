import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        heap = []
        for n, freq in count.items():
            heapq.heappush(heap, (freq, n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for freq,n in heap]