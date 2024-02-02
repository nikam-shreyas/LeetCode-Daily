class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def gen_n_number(n):
            res = []
            start = 1
            for i in range(1, 10-n+1):
                def create_num(start):
                    res = []
                    for i in range(n):
                        res.append(chr(ord('0')+start+i))
                    return int(''.join(res))
                num = create_num(i)
                if low<=num<=high:
                    res.append(num)
            return res
        res = []
        for i in range(len(str(low)), len(str(high))+1):
            res.extend(gen_n_number(i))
        return res
            
                    
        
        
