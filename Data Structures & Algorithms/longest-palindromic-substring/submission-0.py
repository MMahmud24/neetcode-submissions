class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if n == 0:
            return ""

        best = ""

        def expand_from_center(s, i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i-=1
                j+=1

            return s[i+1:j]

        for i in range(len(s)):
            odd = expand_from_center(s, i, i)
            even = expand_from_center(s,i,i+1)
        
            if len(odd) > len(best):
                best = odd
            if len(even) > len(best):
                best = even

        return best