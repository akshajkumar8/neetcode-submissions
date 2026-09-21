class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        result = []
        n = len(word1)
        m = len(word2)
        while i < n or j < m:
            if i < n:
                result.append(word1[i])
            if j < m:
                result.append(word2[j])
            i += 1
            j += 1
        return "".join(result)