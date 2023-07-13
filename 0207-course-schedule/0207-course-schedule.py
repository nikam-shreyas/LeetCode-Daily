class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        nodesVisited = 0
        
        for start, end in prerequisites:
            adj[end].append(start)
            indegree[start]+=1
        
        queue = deque()
        
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        
        while queue:
            curr = queue.popleft()
            nodesVisited += 1
            for nextnode in adj[curr]:
                indegree[nextnode]-=1
                if indegree[nextnode]==0:
                    queue.append(nextnode)
        
        return nodesVisited==numCourses
                    
                    
                