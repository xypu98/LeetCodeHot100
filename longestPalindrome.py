class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        matrix = [[0 for i in range(n)] for j in range(n)]
        maxlen = 1
        st =0

        for i in range(n):
            matrix[i][i]=1
        

        for m in range(2,n+1):
            for k in range(n-m+1):
                j=k+m-1
                if (s[k]!=s[j]):
                    continue
                if (m>2 and matrix[k+1][j-1]==0):
                    continue
                matrix[k][j]=1
                maxlen = m
                st = k

        return s[st:st+maxlen]
