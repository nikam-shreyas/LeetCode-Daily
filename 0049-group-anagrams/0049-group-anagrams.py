from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for str_ in strs:
            ans[''.join(sorted(list(str_)))].append(str_)
        return ans.values()