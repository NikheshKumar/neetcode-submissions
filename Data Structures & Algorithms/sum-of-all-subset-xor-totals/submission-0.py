class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans = ans|n
        ans = ans * (2**(len(nums)-1))

        return ans
        