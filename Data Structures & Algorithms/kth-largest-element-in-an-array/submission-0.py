class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_index = len(nums) - k

        def f(l,r):
            p = l
            for i in range(l,r):
                if nums[i] <= nums[r]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p>target_index:
                return f(l, p-1)
            elif p<target_index:
                return f(p+1, r)
            elif p==target_index:
                return nums[p]

        ans = f(0, len(nums)-1)
        return ans



        