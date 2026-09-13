import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        smallest_pairs = []

        for i in range(min(k, len(nums1))):
            sum_vals = nums1[i] + nums2[0]
            heapq.heappush(heap, (sum_vals, (i, 0)))

        while heap and len(smallest_pairs) < k:
            _, (i, j) = heapq.heappop(heap)
            smallest_pairs.append([nums1[i], nums2[j]])
            if j+1 <= len(nums2)-1:
                sum_vals = nums1[i] + nums2[j+1]
                heapq.heappush(heap, (sum_vals, (i, j+1)))

        return smallest_pairs