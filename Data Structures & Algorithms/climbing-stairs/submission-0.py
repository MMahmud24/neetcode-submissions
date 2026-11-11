class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        prev = 1
        curr = 2
        for i in range(3,n+1):
            new = curr + prev
            prev = curr
            curr = new

        return curr