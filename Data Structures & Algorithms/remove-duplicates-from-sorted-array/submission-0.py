class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()

        l = 0

        for i in range(len(nums)):
            if nums[i] not in s:
                nums[l] = nums[i]
                s.add(nums[i])
                l+=1

        return l