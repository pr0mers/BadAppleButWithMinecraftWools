import cv2
import os
import time
bas = time.time()
vid = cv2.VideoCapture("Bad Apple.mp4")
os.makedirs("BadAppleFrames", exist_ok = True)
framesay=0;
while True:
    ret, frame=vid.read()
    if not ret:
        break
    path=os.path.join("BadAppleFrames", f"frame{framesay}.png")
    #path=os.path(f"BadAppleFrames\frame{framesay}.png")
    cv2.imwrite(path,frame)
    framesay=framesay+1
vid.release()
print(f"Toplam geçen süre: {time.time()-bas} saniye")
