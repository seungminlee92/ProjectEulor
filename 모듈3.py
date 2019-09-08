def prime_factor(n):
    i = 2
    while n != 1 :
        if n%i == 0:
            print(n,i)
            n/=i
        else:
            i+=1
    return i

print(prime_factor(600851475143))