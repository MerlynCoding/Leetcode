class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction=defaultdict(list)
        for i in strs:
            a=''.join(sorted(i))
            diction[a].append(i)
        a=list(diction.values())
        return a