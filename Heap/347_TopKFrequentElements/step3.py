from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = Counter(nums)
        topk = sorted(num_to_count, key=lambda key: num_to_count[key], reverse=True)[:k]
        return topk