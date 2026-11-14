class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices

        stack = []

        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                j = stack.pop()
                ans[j] = ans[j] - p

            stack.append(i)

        return ans
