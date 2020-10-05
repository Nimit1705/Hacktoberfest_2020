f=open("test.txt","r")
print("File Name: ",f.name)
print("File Mode: ",f.mode)
print("Is file Readable: ",f.readable())
print("Is file Closed: ",f.closed())
f.close
print("Is File closed: ",f.closed())
