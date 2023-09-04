class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<int> numset(nums.begin(), nums.end());
        set<vector<int>> ans;
        sort(numset.begin(), numset.end());
        int n = numset.size();
        for(int i=0;i<n-2;i++){
            int left = i+1;
            int right = n-1;
            while(left<right){
                int sum = numset[i]+numset[left]+numset[right];
                if(sum==0){
                    vector<int> temp = {numset[i], numset[left], numset[right]};
                    ans.insert(temp);
                    left+=1;
                    right-=1;
                }
                else if(sum>0){
                    right-=1;
                }
                else{
                    left+=1;
                }
            }
        }
        return vector<vector<int>>(ans.begin(), ans.end());
            
    }
};