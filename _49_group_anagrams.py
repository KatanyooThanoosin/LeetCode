class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            sw="".join(sorted(i))
            if sw in d:d[sw].append(i)
            else:d[sw]=[i]
        return d.values()
