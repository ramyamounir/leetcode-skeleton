
class Solution:
    def isHappy(self, n: int) -> bool:

        def power(val):
            val_str = str(val)
            res = 0
            for v in val_str:
                res += int(v)**2
            return res

        slow, fast = n, n

        while True:
            fast = power(power(fast))
            slow = power(slow)

            if fast == 1 or slow == 1: return True
            if fast == slow: return False

        
