class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        for ch in s:
            if ch in ['{', '[', '(']:
                list.append(ch)
            else:
                if not list:
                    return False
                if ch is '}':
                    if list[-1] is not '{':
                        return False
                    else:
                        list.pop()
                if ch is ']':
                    if list[-1] is not '[':
                        return False
                    else:
                        list.pop()
                if ch is ')':
                    if list[-1] is not '(':
                        return False
                    else:
                        list.pop()
        return False if list else True