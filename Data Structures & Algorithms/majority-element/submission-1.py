class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        max_val = 0
        res = 0

        for key, value in counter.items():
            if value > max_val:
                max_val = value
                res = key

        return res