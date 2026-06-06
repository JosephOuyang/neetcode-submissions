from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for word in strs:
            frequencies = [0] * 26
            for ch in word:
                index = ord(ch) - ord('a')
                frequencies[index] += 1
            anagramMap[tuple(frequencies)].append(word)
        return list(anagramMap.values())
        