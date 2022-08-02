from __future__ import print_function
import cv2 as cv

# algo background subtractor == 'MOG2'or "KNN":
backSub = cv.createBackgroundSubtractorMOG2()

capture = cv.VideoCapture(0)

# star the video capture
while True:
    ret, frame = capture.read()
    if frame is None:
        break

    # update the background model at each frame captured
    fgMask = backSub.apply(frame)


    cv.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    # show video stream
    cv.imshow('Frame', frame)
    # show mask stream
    cv.imshow('FG Mask', fgMask)

    # press "q" to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
