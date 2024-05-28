from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        group_anagram = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            group_anagram[sorted_s].append(s)

        for value in group_anagram.values():
            result.append(value)
        return result
