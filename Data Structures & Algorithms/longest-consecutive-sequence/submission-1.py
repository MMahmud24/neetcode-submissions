class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        starts = defaultdict(int)
        seen = set()
        s = set(nums)

        for i in range(len(nums)):
            x = nums[i]
            if x in seen:
                continue
            if x+1 in starts:
                starts[x] = starts[x+1] + 1
                continue
            starts[x] = 1
            while x+1 in s:
                starts[nums[i]] += 1
                seen.add(x+1)
                x = x+1

        return max(starts.values())

