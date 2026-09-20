class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        n = len(nums)

        while left < n:
            if nums[left] == 0:
                break
            left += 1

        right = left
        while right < n and left < n:
            if nums[right] != 0:
                temp = nums[right]
                nums[right] = 0
                nums[left] = temp
                left += 1

            right += 1
