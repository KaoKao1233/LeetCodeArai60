class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dic = {")":"(", "}":"{", "]":"["}
        open_brackets = []

        for x in s:
            if x not in brackets_dic:
                open_brackets.append(x)
            else:
                if len(open_brackets) == 0 or brackets_dic[x] != open_brackets.pop():
                    return False
        
        return True


# エッジケース確認後
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dic = {")":"(", "}":"{", "]":"["}
        open_brackets = []

        if len(s) % 2 == 1:
            return False

        for x in s:
            if x not in brackets_dic:
                open_brackets.append(x)
            else:
                if len(open_brackets) == 0 or brackets_dic[x] != open_brackets.pop():
                    return False
        
        if len(open_brackets) != 0:
            return False
        else:
            return True
