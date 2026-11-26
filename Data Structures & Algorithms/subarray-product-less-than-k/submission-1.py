class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if min(nums)>=k or k<=1:
            return 0

        l = 0
        r = 0
        count = 0

        temp = 1

        while l<len(nums) and r<len(nums):
            temp = temp * nums[r]
            while temp>=k:
                temp //= nums[l]
                l += 1
            count += r - l + 1
            r+=1


        return count


        