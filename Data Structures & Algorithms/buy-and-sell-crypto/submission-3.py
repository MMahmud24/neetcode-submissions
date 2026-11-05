class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                max_p = max(max_p, prices[r] - prices[l])

        return max_p



