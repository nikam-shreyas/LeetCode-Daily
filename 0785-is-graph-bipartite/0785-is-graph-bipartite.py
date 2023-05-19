class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 1. start with a node
        # 2. put it in red set
        # 3. get all its neighbors
        #   3.1 if neighbor is already visited, check if it is in the opposite set of the current color         
        #       if not return false
        #   3.2 put it in appropriate set and start iterating again
        # do this for all nodes
        # return true
        n = len(graph)
        not_visited = set([i for i in range(n)])
        red_set = set()
        blue_set = set()
        color = 1
        while not_visited:
            queue = deque([not_visited.pop()]) 
            red_set.add(queue[0])
            color=1
            while queue:
                # print(queue, red_set, blue_set)
                qlen = len(queue)
                for _ in range(qlen):
                    curr = queue.popleft()
                    for nxtnode in graph[curr]:
                        if nxtnode in not_visited:
                            if color==1:
                                blue_set.add(nxtnode)
                            else:
                                red_set.add(nxtnode)
                            queue.append(nxtnode)
                            not_visited.remove(nxtnode)
                        else:
                            if color==1:
                                if nxtnode in red_set:
                                    return False
                            else:
                                if nxtnode in blue_set:
                                    return False
                color = 1-color
        return True
                                
                            
                                
            
                        
