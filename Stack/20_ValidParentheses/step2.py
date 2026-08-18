class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        brackets_dic = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        close_brackets = []

        for x in s:
            if x in brackets_dic:
                close_brackets.append(brackets_dic[x])
            else:
                if not close_brackets or x != close_brackets.pop():
                    return False

        return not close_brackets