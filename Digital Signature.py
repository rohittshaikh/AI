from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate keys
private = rsa.generate_private_key(public_exponent=65537, key_size=1024)
public = private.public_key()

msg = b"Hello World"

# Sign message
sig = private.sign(msg, padding.PKCS1v15(), hashes.SHA256())
print("Signature created")

# Verify signature
try:
    public.verify(sig, msg, padding.PKCS1v15(), hashes.SHA256())
    print("Valid: Authentic and unchanged")
except:
    print("Invalid: Message modified or signature incorrect")

