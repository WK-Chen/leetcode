class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': 
            return 0
        n = len(needle)
        m = len(haystack)
        j = 0
        pnext = self.getNext(needle)
        for i in range(m):
            while j > 0 and needle[j] != haystack[i]:
                j = pnext[j]
            if needle[j] == haystack[i]:
                j += 1
                if j == n:
                    return i-n+1
        return -1


    def getNext(self, s: str) -> List[int]:
        n = len(s)
        pnext = [0, 0]
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = pnext[j]
            if s[j] == s[i]:
                j += 1
            pnext.append(j)
        return pnext
        
