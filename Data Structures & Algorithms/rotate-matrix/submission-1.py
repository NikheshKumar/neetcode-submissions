class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix[0])

        for i in range(len(matrix)):
            for j in range(i+1,n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(len(matrix)):
            for j in range(n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]
                matrix[i][n-j-1] = temp

        




        


        