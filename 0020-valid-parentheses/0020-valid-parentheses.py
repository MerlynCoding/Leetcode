class Solution(object):
    def isValid(self,s):
        k=[]
        f={
            "{":"}",
            "(":")",
            "[":"]"
        }

        for i in s :
          if i in f:
            k.append(i)
          elif len(k) == 0 or i!=f[k.pop()]:
            return False
        
        return len(k)==0
        