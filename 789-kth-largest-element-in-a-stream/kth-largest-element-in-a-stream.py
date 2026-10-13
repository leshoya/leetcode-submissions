import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k                              # how many of the largest values we keep
        self.heap = list(nums)                  # copy so we don't change the caller's list
        heapq.heapify(self.heap)                # O(n); heapify works in place and returns None
        while len(self.heap) > k:               # keep only the k largest values
            heapq.heappop(self.heap)            # drop the smallest

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)          # add the new value, O(log k)
        if len(self.heap) > self.k:             # now k + 1 items: one too many
            heapq.heappop(self.heap)            # drop the smallest
        return self.heap[0]                     # smallest of the k largest = k-th largest
# __init__: O(n log n) with this trimming loop; add: O(log k); space: O(k) after trimming.