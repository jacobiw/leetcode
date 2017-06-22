class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        lenli = len(matrix[0])
        for i in xrange(lenli):
            for j in xrange(i,lenli):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in xrange(lenli):
            for j in xrange(lenli/2):
                matrix[i][j], matrix[i][lenli-j-1]=matrix[i][lenli-j-1], matrix[i][j]
