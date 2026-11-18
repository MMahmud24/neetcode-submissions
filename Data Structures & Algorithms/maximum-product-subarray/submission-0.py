class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        best = nums[0]

        for i in range(1,len(nums)):
            x = nums[i]

            candidates = [x, x * curr_max, x*curr_min]

            curr_max = max(candidates)
            curr_min = min(candidates)

            if curr_max > best:
                best = curr_max

        return best
