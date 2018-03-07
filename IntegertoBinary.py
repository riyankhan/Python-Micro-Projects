
#The code is optimized for Python 3
#Following program converts decimal numbers to its binary form
#It only takes input as an integer and not floating value

num = int(input("Enter an integer: "))
decimal_num = num
binary_bits=[]
while num>0:    
    num, remainder = divmod(num, 2)
    binary_bits.append(remainder)
binary_bits= binary_bits[::-1]
print("The Binary coversion of ", decimal_num, " is: ", *binary_bits, sep='')
