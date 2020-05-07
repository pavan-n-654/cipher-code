"""
        positive shift values moves the text backwards
        eg: "A" with shift = 1 means "Z"
        likewise "A" with shift = -1 means "B"
"""
from datetime import datetime
from Cipher_code import decode, encode                #importing decode, encode from Cipher_code.py

def main():
	cipher = input("Enter your choice \"e\" (encode file) \"d\" (decode file)or enter 'ex' for exit: ")
	
	
	check(cipher)

def check( cipher):
	try:
		if cipher.lower() == 'ex' : exit()
		file = input("\nEnter the file name: ")         #ask user for the file name
		fp =open(file, mode = "r")            #opening source file in read mode
		
		lines = list()                        #making list of all lines
		for line in fp.readlines():
			lines.append(line.strip())
		fp.close()
		if cipher.lower() == 'e': encode_file(lines)
		elif cipher.lower() == 'd': decode_file(lines)
		
		else: raise Exception("Invalid choice")
	except Exception as ex:
		print("Error: %s"%ex)
		main()
		
def encode_file( lines):
	en_file = input("Enter the target file name: ")
	en = open(en_file,mode = "a")
	sh = int(input("Enter the shift value: "))
	print("Start".center(80,'#'),file = en)
	print("#",datetime.now().strftime("Year = %Y, Month = %B, Date = %d, day = %A, Time = %H:%M:%S").center(76," "),"#",file = en)
	print("#"*80,file = en)
	for line in lines:
		for al in line:
			print(encode(al, int(sh)%26), end="", file = en) #calling the function
		print(file=en)
	print("End".center(80,'*'),'\n',file = en)
	en.close()
	main()


def decode_file(lines):
	de_file = input("Enter the target file name: ")
	de = open(de_file, mode = 'a')  #opening target file in create and write mode
	sh = input("Enter the shift value or \"n\": ")

	if sh == 'n':
		for sh in range(0,26):        #deciphering for all values
			print("Start".center(80,'#'),file = de) #dumping print statements into the file decoded.txt
			print("#",datetime.now().strftime("Year = %Y, Month = %B, Date = %d, day = %A, Time = %H:%M:%S").center(76," "),"#",file = de)
			print('#',f"Shift value = {sh}".center(76," "),'#',file = de)
			print("#"*80, file = de)
			for line in lines:
				for al in line:
					print(decode(al, sh), end="", file = de) #calling the function
				print(file=de)
			print("End".center(80,'*'),'\n',file = de)
	
	elif type(int(sh))==int:                    #deciphering for a single vslue
		print("Start".center(80,'#'),file = de)
		print("#",datetime.now().strftime("Year = %Y, Month = %B, Date = %d, day = %A, Time = %H:%M:%S").center(76," "),"#",file = de)
		print("#"*80, file = de)
		for line in lines:
			for al in line:
				print(decode(al, int(sh)%26), end="", file = de) #calling the function
			print(file=de)
		print("End".center(50,'*'),'\n',file = de)
	de.close()
	main()
if __name__ == "__main__": main()
