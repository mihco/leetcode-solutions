class Solution:
    def isValid(self, s: str) -> bool:
        brac_pairs = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for c in s:
            if c in brac_pairs:
                if stack and stack[-1] == brac_pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False