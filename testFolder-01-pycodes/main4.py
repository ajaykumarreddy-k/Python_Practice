#copying the same file using the rb especially for the image - >
file = open("image.png", "rb")
file1 = open("new_copy_image.png","wb")
for content in file:
    file1.write(content)
#basically writing all the string into the new file and adding it up make things simple soo using that is the way to copy the file when it comes to images