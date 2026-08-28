class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0 
        lowest = prices[0]

        for p in prices:
            if p<lowest:
                lowest = p
            ans = max(ans, p-lowest)


        return ans