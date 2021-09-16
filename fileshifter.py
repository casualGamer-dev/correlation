import os
import shutil
source=input("enter the source forlder")
path=input("enter the name of the directory to be sorter  ")
listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.move(source+ "/" + file, path)

