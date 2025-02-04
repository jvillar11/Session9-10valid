fp=open("text.txt","r+") #this is open from reading
print(fp.read()) #read() method gets the entire file content
fp.close() #this is good practice

#same thing using a context manager
with open("text.txt","r+") as f:
    print(f.read())

# NO NEED TO CLOSE
with open("text.txt","r+") as f:
    for line in f:
        print(line, end="")
        print(line.rstrip())