class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str = ""
        for c in s:
            if(c.isnumeric() or c.isalpha()):
                new_str += c
        for i in range(int(len(new_str)/2)):
            if(new_str[i] != new_str[-1-i]):
                return False
        return True