class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        s = str(b)
        count = 0
        for i in s:
            if i == '1':
                count += 1
        return count