
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        not_yet_ready = []

        for i, (enqueue_time, _) in enumerate(tasks):
           # add to not_yet_ready queue, prioritize by enqueue time
           heapq.heappush(not_yet_ready, (enqueue_time, i))

        result = []
        ready_to_process = []
        next_available_processor_time = 1
        while not_yet_ready or ready_to_process:
           # if nothing is ready to process, fast-forward to enqueue time of next-ready task
           if not ready_to_process:
            time = not_yet_ready[0][0]
           # otherwise, fast-forward to next_available_processor_time
           else:
            time = next_available_processor_time

           # add all ready tasks to ready queue, prioritize by processing time then i
           while not_yet_ready and not_yet_ready[0][0] <= time:
            _, i = heapq.heappop(not_yet_ready)
            heapq.heappush(ready_to_process, (tasks[i][1], i))

           # if processor is available and a task is ready, begin top-priority task and update result
           if ready_to_process and next_available_processor_time <= time:
            processing_time, i = heapq.heappop(ready_to_process)
            next_available_processor_time = time + processing_time
            result.append(i)

        return result