import cv2
import time 
import mediapipe
import PoseModule as pm
from datetime import datetime

cap = cv2.VideoCapture('SLR.mp4')
pTime = 0
detector = pm.poseDetector()
legLength = []
start_time = 0
duration = 3
nSecond = 0
elapsed_time = 0
counter = 0

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    
    try: 
        print(lmList[28])
        if not legLength:
            legLength = lmList[28][1] - lmList[24][1]
            raiseHeight = legLength/3
            requiredHeight = lmList[24][2] - raiseHeight
            
        
        if lmList[28][2] < requiredHeight and legLength:#stopped at this part, tricky

            if start_time == 0:
                start_time = time.time()

            elapsed_time = time.time() - start_time
            print(elapsed_time)

            

        else:
            elapsed_time = 0
            start_time = 0

        
        
        cv2.putText(img, str(int(elapsed_time))+ 'sec',(50,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3)
        cv2.putText(img, str(int(counter))+ 'rep',(500,70), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3)

        cv2.circle(img, (lmList[28][1],lmList[28][2]), 15, (255,0,0), cv2.FILLED)
    except:
        pass

    if int(elapsed_time) == duration:
        print('yes yes yes')
        counter += 1

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    #cv2.putText(img, str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    # if 0xFF == ord('q'):
    #     break
