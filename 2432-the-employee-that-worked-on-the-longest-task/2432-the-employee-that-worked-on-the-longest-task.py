class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        id_ = logs[0][0]
        longest_task = logs[0][1]
        for i in range(1, len(logs)):
            if logs[i][1]-logs[i-1][1]>longest_task:
                id_ = logs[i][0]
                longest_task = logs[i][1]-logs[i-1][1]
            elif logs[i][1]-logs[i-1][1]==longest_task:
                id_ = min(id_, logs[i][0])
                # longest_task = logs[i][1]-logs[i][0]
        return id_
        