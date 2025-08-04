class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        soretd_s ="".join(sorted(s))
        soretd_t ="".join(sorted(t))
        if soretd_s == soretd_t:
            return True
        else:
            return False