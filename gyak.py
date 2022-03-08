import cv2
import mediapipe as mp
import time
import camera as htm

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        
        self.mpHands = mp.solutions.hands
        self.hands = mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        
        
        
    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmark:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTION)
            return img           
    
                    
            
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmark[handNo]
            for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    print(id, cx, cy)
                    lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 5, (255,0, 255), cv2.FILLED)
            
        return lmList
    
def init():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(1)
    detector = htm.handDetector()
    
def update():
    succes, img = cap.read()        
    img = detector.findHand(img)
    lmList = detector.findPosition(img)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    return lmList[0][2]
            
def main():
    init()
    while True:
        update()
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitkey(1)
        
if __name__ == "__main__":
    main()