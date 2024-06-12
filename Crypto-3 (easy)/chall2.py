from Cryptodome.Util.number import getPrime, bytes_to_long

Flag = bytes_to_long(b"REDACTED")

n = getPrime(64)*getPrime(64)
e = 65537

ciphertext = pow(Flag, e, n)

print([n, e, ciphertext])
