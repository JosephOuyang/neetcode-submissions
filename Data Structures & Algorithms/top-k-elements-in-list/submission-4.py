from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freqs = defaultdict(int)
        # collect freqs
        for num in nums:
            freqs[num] += 1
        # build freq buckets
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        # organize nums by freq index
        for num in freqs:
            freq = freqs[num]
            buckets[freq].append(num)
        # collect top k most frequent
        for i in range(len(buckets) - 1, 0, -1):
            bucket = buckets[i]
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result


        