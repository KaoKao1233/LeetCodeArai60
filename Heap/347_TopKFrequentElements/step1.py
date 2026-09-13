import heapq
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
        top_k_nums = []

        for num, count in num_to_count.items():
            if len(top_k_nums) < k:
                heapq.heappush(top_k_nums, (count,num))

            elif top_k_nums[0][0] < count:
                heapq.heappushpop(top_k_nums, (count,num))

        return [num for count, num in top_k_nums]
