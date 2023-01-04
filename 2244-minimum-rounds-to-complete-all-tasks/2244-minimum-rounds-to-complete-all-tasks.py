from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasksCounter = Counter(tasks)        
        tCountMin = 0
        for _, count in tasksCounter.items():
            if count==1:
                return -1
            elif count%3==0:
                tCountMin+=count//3
            elif (count-2)%3==0:
                tCountMin+=(count-2)//3+1
            elif (count-4)%3==0:
                tCountMin+=(count-4)//3+2
            else:
                return -1
        return tCountMin
                