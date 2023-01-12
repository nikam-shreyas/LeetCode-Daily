from collections import defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjlist = defaultdict(list)
        for x, y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)
        
        counter = defaultdict(int)
        visited = set()
        visited.add(0)
        ans = [0]*n
            
        def recurse(root, counter, visited):
            i = root
            countercopy = counter.copy()
            for child in adjlist[i]:
                if child not in visited:
                    visited.add(child)
                    counter2 = recurse(child, countercopy.copy(), visited)
                    for j in counter2:
                        counter[j]+=counter2[j]
            counter[labels[i]]+=1
            ans[i] = counter[labels[i]]
            return counter
        
        recurse(0, counter, visited)
        return ans
                