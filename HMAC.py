import hmac , hashlib

def generateMac(message, key):
    msgByte = message.encode()
    keyByte = key.encode()

    mac = hmac.new(msgByte, keyByte , hashlib.sha256).hexdigest()

    return mac

def verifyMac(message,key,received_mac):
    msgByte = message.encode()
    keyByte = key.encode()

    mac = hmac.new(msgByte,keyByte,hashlib.sha256).hexdigest()

    result = hmac.compare_digest(received_mac,mac)

    return result

mac = generateMac("Sachin","Two")
print(mac)
result = verifyMac("Sachin","Two",mac)
print(result)
