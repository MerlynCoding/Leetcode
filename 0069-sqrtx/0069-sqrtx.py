class Solution(object):
    def mySqrt(self, x):
        import math as m 
        if x>=0:
            return int(m.sqrt(x))
        