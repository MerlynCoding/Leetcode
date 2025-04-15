class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cS={}
        ct={}
        for i in range(len(s)):
            cS[s[i]]=1+cS.get(s[i],0)
            ct[t[i]]=1+ct.get(t[i],0)
        
        return cS==ct