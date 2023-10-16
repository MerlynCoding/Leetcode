class Solution(object):
    def generate(self, numRows):
        l=[[0]]*numRows
        for i in range(1,numRows+1):
        # print(l)
            if i<=2:
                l[i-1]=[1]*i
            else:
                l[i-1]=[1]
                for j in range(1,len(l[i-2])):
                    l[i-1].append(l[i-2][j-1]+l[i-2][j])
                l[i-1].append(1)
        return l