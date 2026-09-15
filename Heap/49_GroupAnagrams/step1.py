from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_word_to_strs = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            sorted_word_to_strs[sorted_s].append(s)

        return list(sorted_word_to_strs.values())



# import sys


# a = "a"*100
# print(sys.getsizeof(a))
