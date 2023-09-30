class Solution(object):
    def longestCommonPrefix(self, strs):
        strs=sorted(strs)

        first=strs[0]
        last=strs[-1]
        print(first, last)
        k=[]

        for i in range (0,len(first)):
            if len(last)>i and last[i]==first[i]:
                k.append(last[i])
            else:
                return "".join(k)
        return "".join(k)