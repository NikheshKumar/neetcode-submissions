class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        unique = {n for n in nums if n>0}
        v = 1
        while v in unique:
            v += 1

        return v