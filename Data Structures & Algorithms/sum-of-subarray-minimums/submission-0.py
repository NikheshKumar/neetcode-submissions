class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        k = 10**9 + 7
        ans = 0
        stack = []

        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                i_new, n_new = stack.pop()
                left = i_new - stack[-1][0] if stack else i_new + 1
                right = i - i_new
                ans = (ans + n_new * left * right) % k

            stack.append((i,n))


        for i in range(len(stack)):
            idx, n = stack[i]
            left = idx - stack[i-1][0] if i>0 else idx + 1
            right = len(arr) - idx
            ans = (ans + n * left * right)%k 

        return ans
        
