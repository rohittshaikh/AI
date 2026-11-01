min = ord("a")
max = ord("z")
size = min + max + 1

def encrypt(text,key) :
    result = ""
    for char in text :
        charOrd = ord(char)
        cipher = min + ((charOrd - min + key)%size)
        result += chr(cipher)
    return result

def decrypt(text,key) :
    result = ""
    for char in text :
        charOrd = ord(char)
        plainText = min + ((charOrd - min - key)%size)
        result += chr(plainText)
    return result

text = input("Enter the String").strip().lower()
key = int(input("Enter the key"))
cipher = encrypt(text,key)
print("Cipher text : " ,cipher  )
print("Plain Text : ", decrypt(cipher,key)) 
          
      
