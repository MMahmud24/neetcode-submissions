class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        count = defaultdict(int)
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])

            if (r-l+1) - max_freq > k:
                count[s[l]] -=1
                l+=1

            longest = max(longest, r-l+1)

        return longest


''' 
if lenght of window is more than twice k


ABAABAABAAABBBB

'''