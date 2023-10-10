class Solution(object):
    def grayCode(self, n):
        k=[]
        for i in range(0,2**n):
            k.append(i^(i>>1))
        return k
        