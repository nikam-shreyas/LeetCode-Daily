class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        curr_num = arr[0]
        count = 0
        maxcount = len(arr)//4
        for num in arr:
            if curr_num==num:
                count+=1
                if count>maxcount:
                    return num
            else:
                curr_num = num
                count = 1
        return curr_num