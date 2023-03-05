from collections import defaultdict, deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        adjlist = defaultdict(list)
        for i, num in enumerate(arr):
            adjlist[num].append(i)
        # print(adjlist)
        # queue = [(0,0)]
        # visited = set((0,0))
        # visited.add(0)
        # minsteps = inf
        # while queue:
        #     print(queue)
        #     curr = queue.pop()
        #     visited.add(curr[0])
        #     if curr[0]==len(arr)-1:
        #         minsteps=min(minsteps, curr[1])
        #         continue
        #     if curr[0]-1 not in visited and curr[0]-1>=0:
        #         queue.append((curr[0]-1, curr[1]+1))
        #     if curr[0]+1 not in visited and curr[0]+1<len(arr):
        #         queue.append((curr[0]+1, curr[1]+1))
        #     for n in adjlist[arr[curr[0]]]:
        #         if n not in visited:
        #             queue.append((n, curr[1]+1))
        # return minsteps
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = set([0])  # store layers from start
        visited = {0, n-1}
        step = 0

        other = set([n-1]) # store layers from end

        # when current layer exists
        while curs:
            # search from the side with fewer nodes
            if len(curs) > len(other):
                curs, other = other, curs
            nex = set()

            # iterate the layer
            for node in curs:

                # check same value
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.add(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)

            curs = nex
            step += 1

        return -1