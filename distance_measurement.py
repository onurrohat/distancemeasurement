import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector


cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)



while True :
    success,img = cap.read()

    img,faces = detector.findFaceMesh(img,draw=False)

    if faces :
        face = faces[0]
        pointLeft = face[145]
        pointRight= face[374]
        #cv2.circle(img,pointLeft,5,(255,0,255),cv2.FILLED)
        #cv2.circle(img,pointRight,5,(255,0,255),cv2.FILLED)
        #cv2.line(img,pointLeft,pointRight,(0,200,0),3)
        w,_= detector.findDistance(pointLeft,pointRight)
        W=6.3 #real length of distance between human eyes
        d= 60 # real distance length between camera and me 
        #print(w)

        f = (w*d)/W #focal point

        #print(f)

        f = 438 #average value of focal point

        # distance measurement
        
        d =(W*f)/w

        print(d)

        cvzone.putTextRect(img,f'Depth: {int(d)}cm',(face[10][0]-60,face[10][1]-40),scale=2,colorT=(255,0,0),colorR=(0,255,0))



    cv2.imshow("Imagw",img)

    cv2.waitKey(1)