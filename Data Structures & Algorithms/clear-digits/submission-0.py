class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        digits = [str(i) for i in range(10)]

        for char in s:
            if char in digits:
                if stack:
                    stack.pop() 
            else:
                stack.append(char)

        return "".join(stack)

        