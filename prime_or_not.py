
## prime or not

def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return 'Not Prime Number'
        else:
            return 'Prime Number'
    else:
        return 'Not Prime Number'
a = isPrime(8)
print(a)