class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] if len(strs) > 0 else ''

        for i in range(1, len(strs)):
            if not prefix: break
            string = strs[i]
            for j in range(len(prefix)):
                if j >= len(string) or prefix[j] != string[j]:
                    prefix = prefix[:j]
                    break
        return prefix