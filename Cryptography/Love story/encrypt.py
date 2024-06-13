def to_my_honey(owo):
    return ord(owo) - 0x41

def from_your_lover(uwu):
    return chr(uwu % 26 + 0x41)

def encrypt(billet_doux):
    letter = ''
    for heart in range(len(billet_doux)):
        letters = billet_doux[heart]
        if not letters.isalpha():
            owo = letters
        else:
            uwu = to_my_honey(letters)
            owo = from_your_lover(uwu + heart)
        letter += owo
    return letter

m = "REDACTED"

c = encrypt(m)
print(c)
