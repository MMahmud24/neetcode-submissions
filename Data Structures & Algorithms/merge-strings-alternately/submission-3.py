class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = 0
        l2 = 0
        word1 = list(word1)
        word2 = list(word2)

        m = len(word1)
        n = len(word2)

        combined = []
        while l1 < m and l2 < n:
            combined.append(word1[l1])
            combined.append(word2[l2])
            l1+=1
            l2+=1

        if l1 < m:
            combined.extend(word1[l1:])
        else:
            combined.extend(word2[l2:])

        return "".join(combined)

        

