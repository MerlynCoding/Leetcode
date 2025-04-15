class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=list(s)
        for i in t :
            if i not in s :
                return False
            s.remove(i)
        return True
            
        