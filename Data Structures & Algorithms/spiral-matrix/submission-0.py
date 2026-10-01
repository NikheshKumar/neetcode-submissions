class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        ans = []

        while left < right and top < bottom:

            if not(left < right):
                break
            if not(top < bottom):
                break

            for j in range(left, right):
                ans.append(matrix[top][j])
            top += 1
            
            for i in range(top, bottom):
                ans.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break


            for j in range(right-1, left-1, -1):
                ans.append(matrix[bottom-1][j])
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                ans.append(matrix[i][left])
            left += 1


        return ans



        