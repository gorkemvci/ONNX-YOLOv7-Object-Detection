import cv2
import sys
from random import randint
from yolov7 import YOLOv7
import pybboxes as pbx
model_path = "models/uavmini.onnx"
tracker = cv2.legacy.TrackerCSRT_create()
tracker_name = "csrt"
yolov7_detector = YOLOv7(model_path, conf_thres=0.5, iou_thres=0.5)
video = cv2.VideoCapture('UAV_Examples/uav1.mp4')
if not video.isOpened():
    print('Error while loading the video!')
    sys.exit()
# while bbox == [] :
#     ok, frame = video.read()
#     bbox ,scores, class_ids=yolov7_detector(frame)
#     if bbox != []:
#         bbox = (bbox[0][0],bbox[0][1],bbox[0][2],bbox[0][3])
#     #cv2.imshow('Tracking', frame) 
#     cv2.imshow('Tracking', frame)
#     if cv2.waitKey(1) & 0XFF == 27: # esc
#         break
while True:
    ok, frame = video.read()
    h,w,_= frame.shape
    bbox ,scores, class_ids=yolov7_detector(frame)
    if bbox != []:
        bbox = (bbox[0][0],bbox[0][1],bbox[0][2],bbox[0][3])
        print(bbox)
        bbox = (bbox[0],bbox[1],bbox[2]-bbox[0], bbox[3]-bbox[1])
        print(bbox)
        bbox = cv2.selectROI(frame)
        print(bbox)
      

        #bbox = (bbox[0],bbox[1],bbox[2]-bbox[0], bbox[3]-bbox[1])
        #extract x1, y1 <- merkez, genişlik, yükseklik

        # x1 = int ( float (bbox[0]) * w )

        # y1 = int ( float (bbox[1]) * h )

        # xw = int ( float (bbox[2]) * w / 2 )

        # yw = int ( float (bbox[3]) * h / 2 )



        # #x1,y1, x2,y2 yap

        # startpoint = (x1 - xw, y1 - yw )

        # finalpoint = (x1 + xw, y1 + yw )
        # cv2.rectangle(frame, startpoint, finalpoint, (255, 0, 0), 2)

        # bbox = ( x1 - xw, y1 - yw , x1 + xw, y1 + yw  )
        #print(str(bbox))
        #bbox = (int(bbox[0]*size[1]-(bbox[2]*size[1])/2) ,int( bbox[1]*size[0]-(bbox[3]*size[0])/2) , int(bbox[2]*size[1] ), int(bbox[3]*size[0] ))
        #bbox = pbx.convert_bbox(bbox, from_type="yolo", to_type="voc", image_size=(size[0],size[1]))
        #print(ok)
        if not ok:
            break
        bbox = (bbox[0],bbox[1],bbox[2]-bbox[0], bbox[3]-bbox[1])
        ok, bbox = tracker.update(frame)
        #bbox = (bbox[0],bbox[1],bbox[2]-bbox[0], bbox[3]-bbox[1])
        #print(ok, bbox)
        if ok == True:
            (x, y, w, h) = [int(v) for v in bbox]
            #print(x, y, w, h)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, tracker_name , (100, 20), cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255))
        else:
            cv2.putText(frame, 'Tracking failure!', (100,80), cv2.FONT_HERSHEY_SIMPLEX, .75, (0,0,255))

        

    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27: # esc
        break