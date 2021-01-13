class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_int = str(x)
        last_idx = len(str_int) - 1
        for i in range(last_idx // 2 + 1):
            if str_int[i] != str_int[last_idx - i]:
                return False
        return True