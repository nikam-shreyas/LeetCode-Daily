class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def dist(s1, s2):
            count=0
            for i, j in zip(s1, s2):
                if i!=j:
                    count+=1
            return count==1
        count = 0
        queue = [start]
        visited = set([start])
        while queue:
            q1 = queue[:]
            queue = []
            while q1:
                curr = q1.pop()
                visited.add(curr)
                if curr==end:
                    return count
                for gene in bank:
                    if gene not in visited and dist(gene, curr)==1:
                        queue.append(gene)
                        
            count+=1
        return -1