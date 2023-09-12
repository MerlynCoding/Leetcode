class Solution(object):
    def isPalindrome(self, x):
        b=str(x)
        a=b[::-1]
        if a==b:
            return True
        else :
            return False
        