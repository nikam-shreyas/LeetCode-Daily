class Solution {
public:
    int numberOfBeautifulIntegers(int low, int high, int k) {
        int beautifulCount = 0;
        int x=low%k;
        if(x!=0){
            low+=k-x;
        }
        if(high>1e8){
            high=1e8;
        }
        for (int num = low; num <= high; num=num+k) {
            if (isBeautiful(num)) {
                beautifulCount++;
            }
        }
        
        return beautifulCount;
    }
    
private:
    bool isBeautiful(int num) {
        int evenCount = 0;
        int oddCount = 0;

        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
            num /= 10;
        }

        return evenCount == oddCount;
    }
};
