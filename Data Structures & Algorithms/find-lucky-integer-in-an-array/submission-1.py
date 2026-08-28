class Solution:
    def findLucky(self, arr: List[int]) -> int:

        ans = -1
        count = Counter(arr)

        for n, freq in count.items():
            if n==freq:
                ans = max(ans, n)

        return ans
        