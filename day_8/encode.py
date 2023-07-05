alphabet = []
for i in range(65, 91):
    alphabet.append(chr(i + 32))
print("""
Choose command:
    encode: text move forward
    decode: text move backward
    end
    """)
command = input("Choose command:\n")
to_decode = []
to_encode = []
while command != 'end':
    strings = input('Your message:\n').lower()
    shift = int(input("How many steps:\n"))
    prime_shift = shift % 26
    transfer = list(strings)
    if command == 'encode':
        for i in range(len(transfer)):
            for j in range(len(alphabet)):
                if transfer[i] == alphabet[j]:
                    add = alphabet[j - 26 + prime_shift]
                    to_encode.append(add)
            if transfer[i] not in alphabet:
                to_encode.append(transfer[i])
        print(''.join(to_encode))
    if command == 'decode':
        for i in range(len(transfer)):
            for j in range(len(alphabet)):
                if transfer[i] == alphabet[j]:
                    add = alphabet[j - prime_shift]
                    to_decode.append(add)
            if transfer[i] not in alphabet:
                to_decode.append(transfer[i])
        print(''.join(to_decode))
    command = input("Choose command:\n")
