class Solution(object):
    def grayCode(self, n):
        arr=[0]
        for i in range(1,n+1):
            mask=1<<(i-1)
            for j in arr[::-1]:
                arr.append(mask+j)
        return arr
        