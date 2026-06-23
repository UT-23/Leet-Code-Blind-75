class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result=[]
        for row in range(numRows):
            current_row = [1] * (row + 1)
            for j in range(1,row):
                current_row[j] = result[-1][j-1] + result[-1][j]
            result.append(current_row)
        return result

        