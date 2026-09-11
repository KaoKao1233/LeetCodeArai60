import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_elements = []
        nums.sort(reverse=True)

        for num in nums:
            heapq.heappush(self.top_k_elements,num)
            if len(self.top_k_elements) == k:
                break

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_elements,val)

        if len(self.top_k_elements) > self.k:
            heapq.heappop(self.top_k_elements)

        return self.top_k_elements[0]
    

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
