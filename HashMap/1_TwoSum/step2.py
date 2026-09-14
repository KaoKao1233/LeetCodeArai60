from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted((num, i) for i, num in enumerate(nums)) 
        i = 0
        j = len(sorted_nums) - 1
        sum_val = 0

        while i < j:
            sum_val = sorted_nums[i][0] + sorted_nums[j][0]

            if sum_val == target:
                return [sorted_nums[i][1], sorted_nums[j][1]]
            elif sum_val < target:
                i += 1
            elif sum_val > target:
                j -= 1
