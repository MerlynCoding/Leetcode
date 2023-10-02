class Solution(object):
    def lengthOfLastWord(self, s):
        stripped = s.strip()
        strList = stripped.split(" ")
        lastWord = strList[-1]
        return len(lastWord)   
        