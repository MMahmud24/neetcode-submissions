class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            if s[r] not in sett:
                sett.add(s[r])
                longest = max(longest, len(sett))
            else:
                while l < r and s[l] != s[r]:
                    sett.remove(s[l])
                    l+=1
                l+=1

        return longest

