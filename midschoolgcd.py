def prime_factors(m):
    factors = []
    divisor = 2
    while m > 1:
        while m % divisor == 0:
            factors.append(divisor)
            m //= divisor
        divisor += 1
    return factors

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors
#####
number1 = int(input("Enter a number1: "))
M=print("Prime factors of", number1, "are:", prime_factors(number1))

number2 = int(input("Enter a number2: "))
N=print("Prime factors of", number2, "are:", prime_factors(number2))

gcd= [x for x in prime_factors(number1) if x in prime_factors(number2)]

result = 1
for num in gcd:
    result *= num

print("GCD=", result)
