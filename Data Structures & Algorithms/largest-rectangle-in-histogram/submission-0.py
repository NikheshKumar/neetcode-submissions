class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                idx, h = stack.pop()
                max_area = max(max_area, h * (i-idx))
                start = idx
            stack.append((start,heights[i]))

        for i,h in stack:
            max_area = max(max_area, h*(len(heights)-i))

        return max_area
        