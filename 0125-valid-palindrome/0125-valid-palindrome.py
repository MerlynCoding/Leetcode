class Solution(object):
    def isPalindrome(self, s):
        if all(32 <= ord(char) <= 126 for char in s):
            s = ''.join(char for char in s if char.isalnum())
            s=s.lower()
        
            return s==s[::-1]

        