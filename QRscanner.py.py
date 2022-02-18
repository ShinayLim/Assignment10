from pickle import FRAME
from tkinter import Frame
import cv2
import datetime
import webbrowser
#from pyzbar.pyzbar import decode 

cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    success, frame = cap.read()
    if data:
        a = data
        break

    cv2.imshow("QRCODEscanner", img)
    if cv2.waitKey(1) == ord("q"):
        continue

    #for captureinfomartions in decode (frame):
        textFile = open("Log Book.txt", "x")
        textFile.write(f"{captureinfomartions.data.decode('utf-8')}\n" )

        date = datetime.datetime.now()
        textFile.write(date.strftime("Date: %m/%d/%Y \n"))
        textFile.write(date.strftime("Time: %H:%M:%S"))  
        textFile.close()

b = webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()