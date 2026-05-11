class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]= ans till word1 till ith index and word2 till jth
        n1=len(word1); n2 = len(word2)

        if not word1 or not word2:
            return(max(n1,n2))
        
        dp=[[0 for _ in range(n1) ]for _ in range(n2)]

        dp[0][0]= 0 if word1[0]==word2[0] else 1

        for j in range(1,n1):
            dp[0][j]=dp[0][j-1]+(1 if word1[j]!=word2[0] else 0)

        for i in range(1,n2):
            dp[i][0]=dp[i-1][0]+(1 if word1[0]!=word2[i] else 0)

        for i in range(1,n2):
            for j in range(1,n1):
                minie=min([dp[i-1][j],dp[i][j-1],dp[i-1][j-1]])
                
                if dp[i-1][j-1]==minie:
                    dp[i][j]=minie + (1 if word1[j]!= word2[i] else 0)
                else:
                    dp[i][j]=minie +1
        return dp[-1][-1]