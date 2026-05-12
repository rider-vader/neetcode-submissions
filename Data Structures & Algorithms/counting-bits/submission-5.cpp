class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n+1);
        dp[0]=0;if(n>=1)dp[1]=1;
        if(n>1)
        {
        int offset=2;
        for(int i=2;i<=n;i++){
            if(i == offset * 2) {offset *= 2;}
            dp[i] = dp[i - offset] + 1;
        }}
        return dp;
        
    }
};
