class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans = nums[0]
        curr = 0

        for n in nums:
            curr += n  
            ans = max(ans, curr)
            if curr < 0:
                curr = 0


        return ans



        