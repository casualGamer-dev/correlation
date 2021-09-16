from os import access
import cv2
import time
import dropbox
import random
startTime=time.time()
def take_snapshot(): 
 number=random.randint(1,100)
 videoCaptureObject = cv2.VideoCapture(0) 
 result = True 
 while(result):

      ret,frame = videoCaptureObject.read() 
      imageName="img"+str(number)+".jpg"
      cv2.imwrite(imageName,frame) 
      startTime=time.time()
      result = False
 return imageName     
 videoCaptureObject.release() 
 cv2.destroyAllWindows()
def uploadFile(imageName):
   accessToken="N4oQ1MwtTuoAAAAAAAAAAb4i1_cqGS1ZlRvwplaU3ycyyWWEwtCQo-wLmIfUNGI4"
   fileFrom=imageName
   fileto="/securityImage/"+imageName
   dbx=dropbox.Dropbox(accessToken)
   with open(fileFrom,"rb") as e:
            dbx.files_upload(e.read(),fileto)
def main():
    while True:
        if (time.time() - startTime) >=5:
            name=take_snapshot()
            uploadFile(name)
main()
