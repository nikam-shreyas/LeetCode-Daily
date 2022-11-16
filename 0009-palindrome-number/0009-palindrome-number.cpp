class Solution
{
    public:
        bool isPalindrome(int x) {
            if(x<0){
                return false;
            }
            long int n=x;
            long int remain,reverse=0;
            while(n>0){
                remain=n%10;
                reverse=(reverse*10)+remain;
                n=n/10;
            }
         if(x==reverse){
             return true;
         }
         else{
             return false;
         }
        }
};