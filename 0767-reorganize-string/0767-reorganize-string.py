from heapq import heapify, heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count the occurrences of each character in the input string
        counter = Counter(s)
        # Find the maximum occurrence of a character
        maxval = max(counter.values())
        # Calculate the remaining characters after removing the maximum
        rem = len(s) - maxval
        # If remaining characters are less than maxval-1, it's not possible to reorganize
        if rem < maxval - 1:
            return ""
        # Create a max-heap with negative occurrence count and character
        h = [(-val, key) for key, val in counter.items()]
        heapify(h)
        
        ans = ['']
        while h:
            val, currs = heappop(h)
            # If the current character is the same as the last added character
            if currs == ans[-1]:
                # Pop another character from the heap
                val2, currs2 = heappop(h)
                val2 += 1
                # Append the new character to the answer
                ans.append(currs2)
                # If the count of the new character is not zero, push it back to the heap
                if val2 != 0:
                    heappush(h, (val2, currs2))
                # Push the original character back to the heap
                heappush(h, (val, currs))
            else:
                # Append the current character to the answer
                ans.append(currs)
                val += 1
                # If the count of the current character is not zero, push it back to the heap
                if val != 0:
                    heappush(h, (val, currs))
        # Join the characters in the answer list to form the final reorganized string
        return ''.join(ans)
