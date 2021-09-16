file1=input("enter first file  ")
file2=input("enter second file ")
with open(file1,"r") as a:
    aData= a.read()
with open(file2,"r") as b:
    bData= b.read()
with open(file1,"w") as a:
 a.write(bData)
with open(file2,"w") as b:
 b.write(aData)
