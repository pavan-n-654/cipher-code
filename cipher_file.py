"""
        positive shift values moves the text backwards
        eg: "A" with shift = 1 means "Z"
        likewise "A" with shift = -1 means "B"
"""

from Cipher_code import decode        #importin decode from Cipher_code.py
file = input("Enter the file name: ") #ask user for the file name
sh = input("Enter the shift value or enter 'n': ")
fp =open(file, mode = "r")            #opening source file in read mode
de = open("decoded.txt", mode = 'w')  #opening target file in create and write mode
lines = list()                        #making list of all lines
for line in fp.readlines():
	lines.append(line.strip())
if sh == 'n':
        for sh in range(0,26):        #deciphering for all values
                print("Start".center(50,'#'),file = de) #dumping print statements into the file decoded.txt
                for line in lines:
                        for al in line:
                                print(decode(al, sh), end="", file = de) #calling the function
                        print(file=de)
                print("End".center(50,'*'),'\n',file = de)
elif type(int(sh))==int:                    #deciphering for a single vslue
        print("Start".center(50,'#'),file = de)
        for line in lines:
                for al in line:
                        print(decode(al, int(sh)%26), end="", file = de) #calling the function
                print(file=de)
        print("End".center(50,'*'),'\n',file = de)
fp.close()                           #closing files
de.close()
