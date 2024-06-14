# Over all

In this challenge, we get the ciphertext and the code.
Reading the source, we can easily reverse the algorithm to solve it or simply reply to the gpt chat and ask it to solve it for us.

In case there is no source, you will have to guess the Trithemius encryption type, then use the tool to solve it or write the code to solve it yourself.

Note: When there is no source, this challenge will be very difficult, but when there is a source, it is very easy. There are two options: give both the cipher and the source (easy challenge) or give only the cipher, and the source is the hint (opening the hint will lose half of the score of the problem or something like that).

# Decoder

```
def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def decrypt(m):
    c = ''
    for i in range(len(m)):
        ch = m[i]
        if not ch.isalpha():
            ech = ch
        else:
            chi = to_identity_map(ch)
            ech = from_identity_map(chi - i)
        c += ech
    return c

text = "KJOL_T_ZCTS_ZV_CQKLX_NDFKZTUC."
print (decrypt(text))
```

Flag: `OSCTF{KIMI_O_SUKI_NI_NATTE_SHIMATTA.}`
