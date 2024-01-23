class Solution:
    def maxLength(self, arr: List[str]) -> int:
        newarr = []
        for word in arr:
            if len(set(word))==len(word):
                newarr.append(word)
        d = defaultdict(set)
        for word in newarr:
            d[word] = set(word)
            for u in list(d.keys()):
                if d[u].intersection(set(word))==set():
                    d[u+word] = d[u].union(set(word))
        maxlen = 0
        maxword = None
        for word in d:
            if len(word)>maxlen:
                maxlen = len(word)
                maxword = word
        # print(d)
        return maxlen