class Solution:
    def printNumbers(self, i: int, n: int):
        # Your code goes here
        if i > n: 
            return
        print(i)
        self.printNumbers(i + 1, n)
        
if __name__ == "__main__":
    ob = Solution()
    ob.printNumbers(1, 7)