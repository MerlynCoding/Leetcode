class Solution(object):
    def climbStairs(self, n):
        if n<=0:
            return 0
        sequence=[0,1]
        nex_val=0
        while len(sequence)<=n+1:
            nex_val=sequence[len(sequence)-1]+sequence[len(sequence)-2]
            sequence.append(nex_val)
        return nex_val
    
        