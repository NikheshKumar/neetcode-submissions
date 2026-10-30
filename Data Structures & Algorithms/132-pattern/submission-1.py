class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)

        middle = -float("inf")

        for i in range(n-1,-1,-1):

            if nums[i] < middle:
                return True

            while stack and nums[i] > stack[-1]:
                middle = stack.pop()
            
            stack.append(nums[i])


        
        return False
        
