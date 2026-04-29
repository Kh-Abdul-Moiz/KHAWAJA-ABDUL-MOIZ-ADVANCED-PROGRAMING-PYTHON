#By listing the first six prime numbers: , and , we can see that the th prime is .
#What is the  st prime number?

#Still understanding the logic 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check up to sqrt(n)
        if n % i == 0:
            return False
    return True


count = 0
num = 1

while count < 10001:
    num += 1
    if is_prime(num):
        count += 1

print("The 10001st prime number is:", num)