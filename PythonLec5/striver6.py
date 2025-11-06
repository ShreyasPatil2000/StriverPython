class Solution:    
    def palindromeCheck(self, s: str, n: int, i: int):
        if n <= 1:
            return True
        if i >= n // 2:
            return True
        if s[i] != s[n-1-i]:
            return False
        return self.palindromeCheck(s, n, i + 1)
    
if __name__ == "__main__":
    ob = Solution()
    n = len("toria")
    i = 0
    print(ob.palindromeCheck("toria", n, i))
    # Check for Hannah