class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        dp = [0] * n
        
        def dfs(i):
            if dp[i] != 0:
                return dp[i]
            
            max_steps = 1
            
            for x in range(1, d + 1):
                j = i + x
                if j >= n or arr[j] >= arr[i]:
                    break
                max_steps = max(max_steps, 1 + dfs(j))
                
            for x in range(1, d + 1):
                j = i - x
                if j < 0 or arr[j] >= arr[i]:
                    break
                max_steps = max(max_steps, 1 + dfs(j))
                
            dp[i] = max_steps
            return dp[i]
        
        return max(dfs(i) for i in range(n))
