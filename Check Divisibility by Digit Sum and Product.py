class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n 
        summ = 0
        product = 1

        while n > 0:
            digit = n % 10
            summ += digit
            product *= digit
            n //= 10

        divisor = summ + product
        
        return num % divisor == 0
