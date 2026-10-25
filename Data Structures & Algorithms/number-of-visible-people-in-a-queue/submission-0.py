class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0]*n
        stack = []

        for i,h in enumerate(heights):
            while stack and h>heights[stack[-1]]:
                res[stack.pop()] += 1

            if stack:
                res[stack[-1]] += 1

            stack.append(i)

        return res

        