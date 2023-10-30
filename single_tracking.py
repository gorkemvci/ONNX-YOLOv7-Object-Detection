import cv2
import sys
from random import randint


tracker = cv2.legacy.TrackerCSRT_create()

video = cv2.VideoCapture(0)
if not video.isOpened():
    print('Error while loading the video!')
    sys.exit()

ok, frame = video.read()
if not ok:
    print('Erro while loading the frame!')
    sys.exit()
print(ok)

bbox = cv2.selectROI(frame) 
print(bbox)

ok = tracker.init(frame, bbox)
print(ok)

colors = (randint(0, 255), randint(0,255), randint(0, 255)) 
print(colors)

while True:
    ok, frame = video.read()
    if not ok:
        break

    ok, bbox = tracker.update(frame)
    if ok == True:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), colors, 2)
    else:
        cv2.putText(frame, 'Tracking failure!', (100,80), cv2.FONT_HERSHEY_SIMPLEX, .75, (0,0,255))

    cv2.putText(frame, 'CSRT', (100, 20), cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255))

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27: # esc
        break
























