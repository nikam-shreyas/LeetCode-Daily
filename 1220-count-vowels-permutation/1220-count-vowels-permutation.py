class Solution:
    def countVowelPermutation(self, n: int) -> int:
        followers = {
            '#':['a', 'e', 'i', 'o', 'u'],
            'a':['e'],
            'e':['a','i'],
            'i':['a','e','o','u'],
            'o':['i','u'],
            'u':['a']
        }
        dp = {}
        modu = pow(10, 9)+7
        def recurse(curr_char, curr_len):
            if (curr_char, curr_len) in dp:
                return dp[(curr_char, curr_len)]
            if curr_len==n:
                dp[(curr_char, curr_len)] = 1
                return 1
            temp = 0
            for next_char in followers[curr_char]:
                temp = (temp+recurse(next_char, curr_len+1))%modu
            dp[(curr_char, curr_len)] = temp
            return temp
        return recurse('#', 0)