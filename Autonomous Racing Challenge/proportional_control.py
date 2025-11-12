import cv2
import HAL  
import WebGUI  

kp = 0.0115
err = 0
vel = 6.5

while True:
    try:
        img = HAL.getImage()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        red_mask = cv2.inRange(hsv, (0,125,125), (30,255,255))
        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        M = cv2.moments(contours[0])

        if M["m00"] != 0:
            cX = M["m10"] / M["m00"]
            cY = M["m01"] / M["m00"]
        else:
            cX, cY = 0, 0

        err = 320 - cX
        if cX > 0:
            if abs(err) > 50:
                vel = 3.5
                HAL.setV(vel)
            else:
                vel = vel + 0.03
                vel = min(vel, 30)
                HAL.setV(vel)
            HAL.setW(kp * err)
        WebGUI.showImage(red_mask)
    except:
        print("An exception occurred") 

 
