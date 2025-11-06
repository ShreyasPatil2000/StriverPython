class Solution:
    def fib(self, n: int):
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    
if __name__ == "__main__":
    ob = Solution()
    print(ob.fib(6))