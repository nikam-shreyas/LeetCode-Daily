class Solution:
    def checkString(self, s: str) -> bool:
        flag = True
        for char in s:
            if char=='a':
                if not flag:
                    return False
            else:
                flag=False
        return True