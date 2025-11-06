class Solution:
    def factorial(self, n: int) -> int:
        # Your code goes here
        if n == 1: 
            return 1
        return n * self.factorial(n - 1)
        
if __name__ == "__main__":
    ob = Solution()
    print(ob.factorial(6))