class Solution:
    def intToRoman(self, num: int) -> str:
        reverse_dictionary = {1:'I',
                      5:'V',
                      10:'X',
                      50:'L',
                      100:'C',
                      500:'D',
                      1000:'M',
                      4: 'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
        keys = list(reverse_dictionary.keys())
        keys.sort()
                
        ans = []
        k = len(keys)-1
        while num>0:
            # print(num, keys[k])
            if num>=keys[k]:
                ans.append(reverse_dictionary[keys[k]])
                num-=keys[k]
            else:
                k-=1
        return ''.join(ans)
        
        
        
        
        
        
        
