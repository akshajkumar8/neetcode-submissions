class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)
            total = 0
            current = n

            while current:
                digit = current % 10
                total += digit * digit
                current //= 10
            
            n = total

        return True