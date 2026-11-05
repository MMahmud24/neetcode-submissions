class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mapping = defaultdict(int)

        for num in nums:
            mapping[num] += 1

        heap = []
        for key, value in mapping.items():
            heapq.heappush(heap, (-1*value, key))

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res