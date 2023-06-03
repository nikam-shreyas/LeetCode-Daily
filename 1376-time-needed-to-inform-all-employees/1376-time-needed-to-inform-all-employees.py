class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        adj = {}
        for employee, manager in enumerate(managers):
            if manager==-1:
                continue
            if manager in adj:
                adj[manager].append(employee)
            else:
                adj[manager] = [employee]
        print(adj)
        def dfs(person, time):
            if person not in adj:
                return 0
            temp = []
            for subordinate in adj[person]:
                temp.append(dfs(subordinate, time))
            return informTime[person]+max(temp)
        
        return dfs(headID, 0)