class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        mostFrequent = []
        # track frequencies of each distinct number
        for num in nums:
            frequencies[num] += 1
        # bucket index represents freq
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        # put numbers into buckets based on freq
        for num in frequencies:
            freq = frequencies[num]
            buckets[freq].append(num)
        j = len(buckets) - 1
        while len(mostFrequent) < k:
            currBucket = buckets[j]
            for num in currBucket:
                mostFrequent.append(num)
                if len(mostFrequent) == k:
                    return mostFrequent
            j -= 1



            

        

        