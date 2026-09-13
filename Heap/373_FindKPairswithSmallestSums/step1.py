import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        smallest_sums = []

        for i in range(min(k,len(nums1))):
            sum_vals = nums1[i] + nums2[0]
            heapq.heappush(heap, (sum_vals, (i, 0)))

        for _ in range(k):
            sum_vals, (x, y) = heapq.heappop(heap)
            smallest_sums.append((nums1[x], nums2[y]))
            if y <= len(nums2) -2:
                heapq.heappush(heap, ((nums1[x] + nums2[y+1]), (x, y+1)))

        return smallest_sums