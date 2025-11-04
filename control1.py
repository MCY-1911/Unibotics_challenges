import cv2
import HAL  
import WebGUI  

kp = 0.0118
ki = 0.0001
kd = 0.0001

err_old = 0
err_total = 0

# kp * eer + ki * errtotal + Kd * (err - errOld)

i = 0
while True:

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
        

    if cX > 0:
        err = 320 - cX
        if err > 80:
            HAL.setV(4)
            HAL.setW(kp * err)
        else:
            HAL.setV(7)
            HAL.setW(kp * err)
    i = i + 1
    print(i)        

    WebGUI.showImage(red_mask)
