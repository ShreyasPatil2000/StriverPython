class Solution:
    def isPrime(self, n: int) -> bool:
        #your code goes here
        if n <= 1:
            return False
        for i in range(2, n // 2):
            if n % i == 0:
                return False 
        return True
        
if __name__ == "__main__":    
    ob = Solution()
    print(ob.isPrime(97))