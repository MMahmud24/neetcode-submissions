class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        n = len(nums)
        for i in range(n):
            if i >= n-k:
                break
            while n-k > i and nums[i] == val:
                k+=1
                nums[i], nums[n-k] = nums[n-k], nums[i]

        return n-k

            
       
        