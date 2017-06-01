# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n < 0):
            return 0
        
        if(n == 1):
            return 1
        
        steps = [1,2]
        
        for x in range(2,n):
            count = steps[0] + steps[1]
            steps[0] = steps[1]
            steps[1] = count
            
        return steps[1]
