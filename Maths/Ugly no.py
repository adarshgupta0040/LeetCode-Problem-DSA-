Intuition
Check Simply factors of given no.

Approach
keep dividing the no. by 2,3,5 only till n>1 and if the no. is not divisible by all three nos. then break and and check the no. is equal to 1 so return True else False. (Simple Maths)

Complexity
Time complexity: O(N)
Space complexity: O(1)
  
  
Code
class Solution:
    def isUgly(self, n: int) -> bool:
        while(n>1):
            if n%2==0:
                n=n//2
            elif n%3==0:
                n=n//3
            elif n%5==0:
                n=n//5
            else:
                break
        
        if n==1:
            return True
        else:
            return False
