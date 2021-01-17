import cv2

cameraCapture = cv2.VideoCapture(0)

while cv2.waitKey(1) == -1:
    success, frame = cameraCapture.read()
    if success:
        # Real-time image processing happens here:
        frame[:,:,0] = 0
        ###################
        cv2.imshow('Output', frame)
    else:
        print("Could not read the camera stream.")
        break

cv2.destroyWindow()
cameraCapture.release()