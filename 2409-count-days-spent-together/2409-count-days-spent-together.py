from collections import Counter
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1, len(days_in_month)):
            days_in_month[i]+=days_in_month[i-1]
        # print(days_in_month)
        days_ = [0 for i in range(366)]
        arriveAlice = arriveAlice.split('-')
        leaveAlice = leaveAlice.split('-')
        arriveBob = arriveBob.split('-')
        leaveBob = leaveBob.split('-')
        aliceStart = days_in_month[int(arriveAlice[0])-1]+int(arriveAlice[1])
        aliceEnd = days_in_month[int(leaveAlice[0])-1]+int(leaveAlice[1])
        bobStart = days_in_month[int(arriveBob[0])-1]+int(arriveBob[1])
        bobEnd = days_in_month[int(leaveBob[0])-1]+int(leaveBob[1])
        for i in range(aliceStart, aliceEnd+1):
            days_[i]+=1
        for i in range(bobStart, bobEnd+1):
            days_[i]+=1
        # print(days_)
        # print(aliceStart, aliceEnd, bobStart, bobEnd)
        return Counter(days_)[2]