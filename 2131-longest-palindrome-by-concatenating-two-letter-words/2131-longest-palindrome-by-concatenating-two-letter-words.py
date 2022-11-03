from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        removal = defaultdict(list)
        removals = []
        n = len(words)
        for i in range(n):
            # print(removal)
            re = words[i][::-1]
            # print(re)
            if re in removal and removal[re] != []:
                removals.append(removal[re].pop())
                removals.append(i)
            else:
                removal[words[i]].append(i)
        for k in sorted(removals, reverse=True):
            del words[k]
        repeats = defaultdict(int)
        for i in words:
            if i[0]==i[1]:
                repeats[i]+=1
        # print(removals)
        ans = (max(list(repeats.values())+[0])+len(removals))*2
        return ans