class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            cur=(columnNumber-1)%26
            res += chr(cur+65)
            columnNumber = (columnNumber-1)//26
        return res[::-1]