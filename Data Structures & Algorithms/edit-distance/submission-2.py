class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i, j):
            # base 
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if (i, j) in dp:
                return dp[(i, j)]

            # match 
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i-1, j-1)
                return dp[(i, j)]

            # does not match
            else:
                dp[(i, j)] = 1 + min(
                    dfs(i-1, j), #insert
                    dfs(i, j-1), # delete
                    dfs(i-1, j-1)) # replace
                return dp[(i, j)]
        return dfs(len(word1)-1, len(word2)-1)
        