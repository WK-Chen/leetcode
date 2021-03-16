class Solution:
    def reverse(self, x: int) -> int:
        raw = x
        if x < 0:
            flag = True
            x = -x
        else:
            flag = False
        
        reverse = 0
        while x != 0:
            reverse = reverse * 10 + x % 10
            x = x // 10
        
        reverse = -reverse if flag else reverse
        if reverse < -pow(2, 31) or reverse > pow(2, 31) -1:
            return 0
        else:
            return reverse