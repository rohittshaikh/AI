from math import gcd

p = int(input("Enter a prime number : " ))
q = int(input("Enter another prime number : " ))

n = p * q
phi = (p-1)*(q-1)

e = int(input("Enter a number that is co-prime with phi : "))

while (gcd(e,phi)) != 1 :
    e = int(input("Enter a number that is co-prime with phi : "))
    
        
for d in range (1,phi):
    if (d*e)%phi==1:
        break

print("public key" , e,",",n)
print( "private Key", d , "," , n)

m = int(input("Enter the message : "))

encrypt = pow(m,e,n)
decrypt = pow(encrypt , d,n)
print(encrypt)
print(decrypt)
