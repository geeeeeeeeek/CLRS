__author__ = 'Tong'
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    # @param n, an integer
    # @return an integer

    sub_problems = None

    def climbStairs(self, n):
        self.sub_problems = [0] * (n + 1)
        if n == 0:
            return 0
        if n > 0:
            self.sub_problems[1] = 1
        if n > 1:
            self.sub_problems[2] = 2
        return self.help_function(n)

    def help_function(self, n):
        if not self.sub_problems[n]:
            self.sub_problems[n] = self.help_function(n - 1) + self.help_function(n - 2)
        return self.sub_problems[n]


print(Solution().climbStairs(8))