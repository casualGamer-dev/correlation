import cv2 
from datetime import date

today = date.today()
def take_snapshot(): 

 videoCaptureObject = cv2.VideoCapture(0) 
 result = True 
 while(result):

      ret,frame = videoCaptureObject.read() 
       
      cv2.imwrite(str(today)+".png",frame) 
      result = False
 videoCaptureObject.release()
 cv2.destroyAllWindows()
take_snapshot()