class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.mirror(matrix)
        self.horizontal(matrix)

    def mirror(self, matrix):
        n = len(matrix)
        for i in range(n//2):
            for j in range(n):
                self.swap(matrix, i, j, n-1-i, j)

    def horizontal(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                self.swap(matrix, i, j, j, i)

    def swap(self, nums, i, j, i_, j_):
        tmp = nums[i][j]
        nums[i][j] = nums[i_][j_]
        nums[i_][j_] = tmp
