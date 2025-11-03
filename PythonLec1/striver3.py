class Solution:
    def studentGrade(self, marks: int)->str:
        if(marks > 100 or marks < 0):
            return "Invalid Grade"
        if(marks >= 90):
            return "Grade A"
        elif(marks < 90 and marks >= 70):
            return "Grade B"
        elif(marks < 70 and marks >= 50):
            return "Grade C"
        elif(marks < 50 and marks >= 35):
            return "Grade D"
        else:
            return "Fail" 
    
if __name__ == "__main__":    
    ob = Solution()
    print(ob.studentGrade(85))