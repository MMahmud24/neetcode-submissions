class Solution:
    def countSubstrings(self, s: str) -> int:
        

        n = len(s)

        def expand_from_center(s,i,j):
            count = 0
            while i >=0 and j < n and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1

            return count

        total = 0
        for i in range(n):
            total += expand_from_center(s,i,i)
            total += expand_from_center(s,i,i+1)

        return total
            
            