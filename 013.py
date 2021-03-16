class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L':50,
                'C':100, 'D':500, 'M':1000,
                'IV': 4, 'IX': 9, 'XL': 40, 'XC':90, 'CD':400, 'CM':900}
        length = len(s)
        flag = False
        for i in range(length):
            if flag:
                flag = False
                continue
            if i+1 != length:
                if s[i:i+2] in dic:
                    output = output + dic[s[i:i+2]]
                    flag = True
                else:
                    output = output + dic[s[i]]
            else:
                output = output + dic[s[i]]
        return output