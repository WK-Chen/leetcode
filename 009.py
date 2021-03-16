class Solution:
    def isPalindrome(self, x: int) -> bool:
        raw = x
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        list_x = []
        while x != 0:
            list_x.append(x%10)
            x = x // 10
        reverse_x = 0
        for idx, digit in enumerate(list_x):
            reverse_x = reverse_x*10 + digit
        if raw == reverse_x:
            return True
        else:
            return False