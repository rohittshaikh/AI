p = int(input("Enter a prime number :"))
g = int(input("Enter a prime number :"))

a = int(input("Enter alice private key :"))
b = int(input("Enter bob private key :"))

A = pow(g,a,p)
B = pow(g,b,p)

AliceSecret = pow(B,a,p)
BobSecret = pow(A,b,p)

print("Alice public value : " , A )
print("Bob public value : " , B )


print("Alice shared secret key value : " , AliceSecret)
print("Bob shared secret key value : " , BobSecret)
