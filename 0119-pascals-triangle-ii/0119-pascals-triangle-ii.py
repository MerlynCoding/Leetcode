class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]

        result = [[1]]
        for i in range(1, rowIndex+1):
            prev_row = result[-1]
            new_row = [1]

            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])

            new_row.append(1)
            result.append(new_row)

        return result[rowIndex]
        