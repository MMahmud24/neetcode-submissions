class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        l = n - 1
        selected = nums[n-k:]
        for i in range(n-k-1, -1, -1):
            nums[i], nums[l] = nums[l], nums[i]
            l-=1

        for i in range(k):
            nums[i] = selected[i]
        




        


''' 

6 7 1 2 5 3 4 

'''