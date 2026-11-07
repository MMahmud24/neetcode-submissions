class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {"(":")", "{":"}", "[":"]"}
        stk = []
        for sym in s:
            if sym in mapping:
                stk.append(sym)
            else:
                if not stk:
                    return False
                if not mapping[stk.pop()] == sym:
                    return False

        if stk:
            return False
        return True

