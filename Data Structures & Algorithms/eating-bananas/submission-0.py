class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)
        ans = high

        while low<=high:
            mid = (low+high) // 2
            hours_taken = 0

            for p in piles:
                hours_taken += math.ceil(p/mid)

            if hours_taken <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        