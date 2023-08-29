class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Initialize counters to track unhappy customers
        left_no = [0] 
        right_yes = [0]

        num_customers = len(customers)

        # Populate left_no_shoes list counting "N" customers from left
        for i in range(num_customers):
            if customers[i] == 'N':
                left_no.append(left_no[-1] + 1) 
            else:
                left_no.append(left_no[-1])

        # Populate right_yes_shoes list counting "Y" customers from right  
        for i in range(num_customers-1, -1, -1):
            if customers[i] == 'Y':
                right_yes.append(right_yes[-1] + 1)
            else:
                right_yes.append(right_yes[-1])

        # Find best closing time 
        best_time = -1
        min_unhappy = float("inf")

        for i in range(num_customers + 1):
            unhappy_custs = right_yes[num_customers - i] + left_no[i]
            if unhappy_custs < min_unhappy:
                min_unhappy = unhappy_custs
                best_time = i

        return best_time
