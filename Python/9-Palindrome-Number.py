class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = -1
        for i in range(len(str(x))//2):
            if(str(x)[i] != str(x)[reverse]):
                return False
            reverse -= 1
        return True