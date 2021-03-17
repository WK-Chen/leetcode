class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min([len(s) for s in strs])
        output = ""
        for i in range(min_len):
            same = strs[0][i]
            for s in strs:
                if s[i] != same:
                    return output
            output = output + same
        return output