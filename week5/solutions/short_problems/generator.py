def genPrimes():
    n = 2
    while n < 50: 
        next = n
        if checkPrime(n):
            yield next
        n = next + 1


def checkPrime(n):
    if n == 2: 
        return True
    for x in range(2,n):
        if n%x == 0:
            return False
    return True

primes = genPrimes()
primes.__next__() # this is not working

for n in genPrimes():
  print (n)