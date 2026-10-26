class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = []

        for char in logs:
            if char=="../":
                if stack:
                    stack.pop()
            elif char=="./":
                continue
            else:
                stack.append(char)


        return len(stack)

        