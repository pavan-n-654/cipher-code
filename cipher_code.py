in_put = '' #This program enables user to encode and decode  


alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
Alpha = [chr(i) for i in range(ord('A'), ord('Z') + 1)]


def decode(y, shift):
    if y in alpha:
        if ord(y) - shift > ord('z'):
            x = ord(y) - shift - ord('z')
            y = chr(ord('a') + 1 + x)
        elif ord(y) - shift < ord('a'):
            x = ord('a') - ord(y) + shift
            y = chr(ord('z') + 1 - x)
        else:
            y = chr(ord(y) - shift)
        return y
    elif y in Alpha:
        if ord(y) - shift > ord('Z'):
            x = ord(y) - shift - ord('Z')
            y = chr(ord('A') + 1 + x)
        elif ord(y) - shift < ord('A'):
            x = ord('A') - ord(y) + shift
            y = chr(ord('Z') + 1 - x)
        else:
            y = chr(ord(y) - shift)
        return y
    else:
        return y



def encode(x, shift):
    if x in alpha:
        if ord(x) + shift > ord('z'):
            y = ord(x) + shift - ord('z') - 1
            x = chr(ord('a') + y)
        elif ord(x) + shift < ord('a'):
            y = ord('a') - (ord(x) + shift)
            x = chr(ord('z') - y)
        else:
            x = chr(ord(x) + shift)
        return x
    elif x in Alpha:
        if ord(x) + shift > ord('Z'):
            y = ord(x) + shift - ord('Z') - 1
            x = chr(ord('A') + y)
        elif ord(x) + shift < ord('A'):
            y = ord('A') - (ord(x) + shift)
            x = chr(ord('Z') - y)
        else:
            x = chr(ord(x) + shift)
        return x
    else:
        return x


def encode_input():
    shift_value = input('Enter the shift value: ')
    if shift_value.isdigit() or int(shift_value) in range(-100, 101):
        statement = input('Enter the statement: ')
        print('Encoded statement is')
        for alphabet in statement:
            num = int(shift_value) % 26
            print(encode(alphabet, num), end='')
        print()
    else:
        print('Enter valid shift value', encode_input(), sep='\n')
    inpu()


def decode_input():
    shift_value = input("Enter the shift value or type 'n' if u don't know the shift value: ")
    statement = input('Enter the statement: ')
    if shift_value.lower() == 'n':
        print('Decoded statement is') #if the user does not know the shift value this would create decoded statements of all the shift values
        for sh in range(0, 26):
            for alphabet in statement:
                print(decode(alphabet, sh), end='')
            print("  shift value =",sh)
    elif shift_value.isdigit() or int(shift_value) in range(-100, 101):
        print('Decoded statement is')
        for alphabet in statement:
            num = int(shift_value) % 26
            print(decode(alphabet, num), end='')
        print()
    else:
        print("Enter valid shift value", decode_input(), sep='\n')
    inpu()



def inpu():
    global in_put
    in_put = input("Enter 'e' to encode statement or 'd' to decode statement or 'ex' to exit: ")
    if in_put.lower() == 'e':
        encode_input()
    elif in_put.lower() == 'd':
        decode_input()
    elif in_put.lower() == 'ex': exit()
    else:
        print('Select correct option')
        inpu()

if __name__ == '__main__': 
	try:
		inpu()
	except Exception as ex:
		print("Error:",ex)
		inpu()











