class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l < r-1:
            m = (l+r) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m

        return min(nums[l], nums[r])