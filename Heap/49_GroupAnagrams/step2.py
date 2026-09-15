from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_word_to_word = defaultdict(list)

        for word in strs:
            sorted_word = str(sorted(word))
            sorted_word_to_word[sorted_word].append(word)

        return list(sorted_word_to_word.values())


# import sys


# a = str("'a',"*100)

# print(sys.getsizeof(a))
