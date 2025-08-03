class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = ''.join(filter(str.isalnum, s)).lower()
        if li == li[::-1]:
            return True
        else:
            return False