class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, bool> mp;
        int n=nums.size();
        for( int i=0;i<n;i++){
            if(mp[nums[i]]){return true;}
            else{mp[nums[i]]=true;}
        }
        return false;
        
    }
};