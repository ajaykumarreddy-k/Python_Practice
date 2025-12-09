file=open("image.png", "rb")#for image its rb here
content = file.read() # we can use readline() and  read and we can  skip the general -> thing and use read() -> prints all soo
#readlines() to read all lines and (number) number goes throgh indexees
#for images only read()
print(content)
file.close()
# Reads the content of sample.txt and prints it line by line
#opening images - >