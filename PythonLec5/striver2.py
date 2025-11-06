class Solution:
    def printNumbers(self, n: int):
        # Your code goes here
        if n == 0: 
            return
        print(n)
        self.printNumbers(n - 1)
        
if __name__ == "__main__":
    ob = Solution()
    ob.printNumbers(7)