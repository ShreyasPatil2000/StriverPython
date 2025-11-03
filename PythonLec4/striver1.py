class Solution:
    def countDigit(self, n: int) -> int:
        count = 0
        while(n > 0):
            n = n//10
            count += 1
        return count
        
if __name__ == "__main__":    
    ob = Solution()
    print(ob.countDigit(85))