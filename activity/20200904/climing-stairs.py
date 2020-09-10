class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        prev_prev, prev = 1, 2
        for i in range(n-2):
            prev_prev, prev = prev, prev_prev + prev
        return prev
