def decypt(text, shift):
    if command == 'decode':
        for i in range(len(transfer)):
            for j in range(len(alphabet)):
                if transfer[i] == alphabet[j]:
                    add = alphabet[j - shift]
                    to_decode.append(add)
        print(''.join(to_decode))