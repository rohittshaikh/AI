def encrypt(text):
    even = ""
    odd = ""
    for i in range (len(text)):
        if i %2==0 :
            even += text[i]
        else :
            odd += text[i]

    return even + odd

def decrypt(text):
    result = ""

    mid = (len(text)+1)//2
    even = text[:mid]
    odd = text[mid:]

    for i in range (len(odd)):
        result += even[i]
        result += odd[i]

    if len(odd) < len(even):
        result += even[-1]

    return result

string = input("Enter the text : " )
cipher = encrypt(string)
print(cipher)
plain = decrypt(cipher)
print(plain)
           
