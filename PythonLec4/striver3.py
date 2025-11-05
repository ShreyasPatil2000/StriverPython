class Solution:
    def isPalindrome(self, n: int) -> bool:
        c_num = n 
        r_num = 0
        if n < 0: 
            return False
        while c_num > 0:
            r = c_num % 10
            r_num = 10 * r_num + r
            c_num = c_num // 10
        if r_num == n:
            return True
        else:
            return False
        
if __name__ == "__main__":    
    ob = Solution()
    print(ob.isPalindrome(999))