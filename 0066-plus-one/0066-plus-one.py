class Solution(object):
    def plusOne(self, digits) :
        digits1=''.join(map(str, digits))
        digits1=int(digits1)+1
        res = [int(x) for x in str(digits1)]
        return res



        