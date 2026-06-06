from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            frequencies = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                frequencies[index] += 1
            anagrams[tuple(frequencies)].append(s)
        return list(anagrams.values())

        
        