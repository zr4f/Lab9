
def encode(password):
    encoded_password = ""
    for digit in str(password):
        # Shift each digit up by 3 numbers
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit
    return encoded_password

while True:
    print("Menu \n____________\n1. Encode \n2. Decode \n3. Quit\n")
    choice = input("Please enter an option:")
    if choice == 1:
        password = input("Please enter your password to encode:")
        encoded = encode(password)
        print("Your password has been encoded and stored!")
    elif choice ==2:
        decoded = decode(encoded)
        print(f"The encoded password is {encoded}, and the original password is {decoded}")
        pass
    elif choice ==3:
        break




