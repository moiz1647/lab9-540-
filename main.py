
print("..........")

a = int(input())


def decrypt(data, shift):
    new_data = ""
    for x in data:
        if ord(x) < 65 + shift:
            diff = ord(x) - 65
            new_data += chr(84 + diff)
        else:
            new_data += chr(ord(x) - 7)

    return new_data


code = int(input("Enter the code to decrypt: "))
# code = "KLMLUKAOLMVYA"
shift = int(input("Enter the shift: "))
# shift = 7
print(decrypt(code, shift))
# 65 to 90
