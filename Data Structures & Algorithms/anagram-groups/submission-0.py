class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        grouped = []
        for s in strs:
            if tuple(sorted(s)) not in anagrams:
                anagrams[tuple(sorted(s))] = [s]
            else:
                anagrams[tuple(sorted(s))].append(s)
        for anagram in anagrams:
            grouped.append(anagrams[anagram])
        return grouped

        