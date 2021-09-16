from collections import Counter
import csv
with open ("./csv files/SOCR.csv", newline="") as f:
 reader=csv.reader(f)
 fileData=list(reader)
fileData.pop(0)
newData=[]
for i in range (len (fileData)):
    num=fileData[i][1]
    newData.append(float(num))
m = len(newData)
data=Counter(newData)
modeDataRange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height , occurence in data.items():
    if 50<float(height)<60:
        modeDataRange["50-60"]+=occurence
    elif 50<float(height)<60:
        modeDataRange["60-70"]+=occurence
    else:
     modeDataRange["70-80"]+=occurence    
modeRange,Modoccurence=0,0
for range , occurence in modeDataRange.items():
    if occurence>Modoccurence:
        modeRange,Modoccurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode=float((modeRange[0]+modeRange[1])//2)
print (mode)