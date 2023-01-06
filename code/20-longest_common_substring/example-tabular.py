

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = f'0{text1}'
        text2 = f'0{text2}'

        self.dp = [[0 for _ in range(len(text2)) ] for _ in range(len(text1))]

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):

                if text1[i] == text2[j]:
                    self.dp[i][j] = 1 + self.dp[i-1][j-1]
                else:
                    self.dp[i][j] = max(self.dp[i-1][j],self.dp[i][j-1])


        return self.dp[-1][-1]
