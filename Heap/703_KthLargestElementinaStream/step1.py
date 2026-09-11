import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k = []
        nums.sort(reverse=True)

        for x in nums:
            heapq.heappush(self.top_k,x)
            if len(self.top_k) == k:
                break

    def add(self, val: int) -> int:
        if len(self.top_k) < self.k:
            heapq.heappush(self.top_k,val)

        else:
            if val <= self.top_k[0]:
                return self.top_k[0]
            heapq.heappushpop(self.top_k,val)

        return self.top_k[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
