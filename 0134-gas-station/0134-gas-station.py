class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        -2 -2 3 -2 3
        """
        # n = len(gas)
        # for i in range(n):
        #     start = i
        #     gas_remaining = 0
        #     flag = True
        #     for j in range(n):
        #         station = (start+j)%n
        #         gas_remaining += gas[station]-cost[station]
        #         if gas_remaining<0:
        #             flag=False
        #             break
        #     if flag:
        #         return i
        # return -1
        candidate, debit, credit = None, 0, 0
	
        for i in range(len(gas)):
            credit += gas[i] - cost[i]
            if credit < 0:
                candidate, debit, credit = None, debit - credit, 0
            elif candidate is None: 
                candidate = i

        return candidate if credit >= debit else -1
                
                