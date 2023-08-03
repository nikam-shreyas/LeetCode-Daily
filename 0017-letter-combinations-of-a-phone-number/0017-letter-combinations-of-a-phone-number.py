class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_map = {
            '2':['a', 'b', 'c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],         
        }
        if digits=='':
            return []
        ans = [[letter] for letter in number_map[digits[0]]]
        i = 1
        while i<len(digits):
            temp = []
            for prev in ans:
                for nxt in number_map[digits[i]]:                    
                    prev.append(nxt)
                    temp.append(prev[:])
                    prev.pop()
            ans = temp[:]
            i+=1
        # print(ans)
        ans = [''.join(each) for each in ans]
        return ans
            