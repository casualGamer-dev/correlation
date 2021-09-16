import dropbox
class Transfer (object):
    def __init__(self,accesToken) :
        self.accesToken= accesToken
    def file_transfer(self,fileFrom,fileto):
        dbx= dropbox.Dropbox(self.accesToken)
        with open(fileFrom,"rb") as e:
            dbx.files_upload(e.read(),fileto)
def main():
    accesToken="N4oQ1MwtTuoAAAAAAAAAAb4i1_cqGS1ZlRvwplaU3ycyyWWEwtCQo-wLmIfUNGI4"
    transfer=Transfer(accesToken)
    filefrom="textswapper.py"
    fileName=input("file name")
    filefolder=input("folder name")
    fileto="/"+filefolder+"/"+fileName
    transfer.file_transfer(filefrom,fileto)
if __name__ == "__main__":
 main()