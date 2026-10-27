class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []

        for i, n in enumerate(nums):
            if not stack or n < nums[stack[-1]]:
                stack.append(i)

        ans = -float("inf")

        for j in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[j]:
                ans = max(j-stack.pop(),ans)

        return ans
