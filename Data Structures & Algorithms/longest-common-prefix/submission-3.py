class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for i in range(1,len(strs)):
            for j in range(len(longest)):
                if j >= len(strs[i]) or longest[j] != strs[i][j]:
                    longest = longest[:j]
                    break

        return longest