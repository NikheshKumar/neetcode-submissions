class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        ans = 0

        for n in nums:
            if (n-1) not in elements:
                x = n
                count = 0
                while x in elements:
                    count += 1
                    x += 1
                ans = max(ans, count)

        return ans
        