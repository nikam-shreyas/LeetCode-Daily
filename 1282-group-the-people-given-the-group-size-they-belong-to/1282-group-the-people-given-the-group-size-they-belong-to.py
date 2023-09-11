from collections import Counter
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_counts = Counter(groupSizes)
    
        # Initialize the result groups
        for size, count in group_counts.items():
            num_groups = count // size
            group_counts[size] = [[] for _ in range(num_groups)]

        group_indices = {size: 0 for size in group_counts}

        # Add each person to the appropriate group
        for person, group in enumerate(groupSizes):

          # Check if current group is full
          if len(group_counts[group][group_indices[group]]) == group:
            group_indices[group] += 1

          # Add person to group  
          group_counts[group][group_indices[group]].append(person)

        result = []

        # Flatten groups into output  
        for groups in group_counts.values():
            result.extend(groups)

        return result