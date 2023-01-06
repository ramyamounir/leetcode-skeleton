

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp = [[-1 for _ in range(len(text2)+1) ] for _ in range(len(text1)+1)]

        def lcs(i, j):

            if text1[i] == '\n' or text2[j] == '\n': 
                self.dp[i][j] = 0
                return 0

            if self.dp[i][j] != -1:
                return self.dp[i][j]

            if text1[i] == text2[j]: 
                result = 1 + lcs(i+1, j+1)
                self.dp[i][j] = result
                return result

            result = max(lcs(i+1,j), lcs(i,j+1))    
            self.dp[i][j] = result
            return result

        text1+= '\n'
        text2+= '\n'
        return lcs(0,0)
