from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        mostFrequent = []
        # track frequencies of each distinct num in nums
        for num in nums:
            frequencies[num] += 1
        # obtain max frequency
        kMostFreq = sorted(list(frequencies.values()))[-k : ]
        # build result
        for num in frequencies:
            freq = frequencies[num]
            if freq in kMostFreq:
                mostFrequent.append(num)
        return mostFrequent

