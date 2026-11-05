class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        starts = defaultdict(int)
        s = set(nums)
        res = 0
        for i in range(len(nums)):
            counter = 1
            if starts[nums[i]]:
                continue
            if nums[i] + 1 in starts:
                starts[nums[i]] = starts[nums[i]+1] + 1
                res = max(res, starts[nums[i]])
                continue
            starts[nums[i]] = 1
            while nums[i] + counter in s:
                starts[nums[i]] += 1
                starts[nums[i] + counter] = -1
                counter+=1

            res = max(res, counter)

        return res

