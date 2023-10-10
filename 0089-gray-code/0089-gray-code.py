class Solution(object):
    def grayCode(self, n):
        i=1
        # add old array
        newArr = [0,1]
        while i< n:
            
            # now add bit value to old reversed values
            for j in range(len(newArr)-1,-1,-1):
                newArr.append((2**i)+newArr[j])
            i+=1
        return newArr
        