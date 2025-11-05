class Solution:
    def GCD(self, n1: int, n2: int)-> int:
        if n1 < n2:
            n2, n1 = n1, n2
        while n2 != 0:
            n1, n2 = n2, n1 % n2
        return n1
        
if __name__ == "__main__":    
    ob = Solution()
    print(ob.GCD(63, 9))