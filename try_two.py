import cv2
import sys
from random import randint
from yolov7 import YOLOv7
import pybboxes as pbx
import time
model_path = "models/best.onnx"
yolov7_detector = YOLOv7(model_path, conf_thres=0.5, iou_thres=0.5)
video = cv2.VideoCapture('UAV_Examples/uav1.mp4')
if not video.isOpened():
    print('Bir Hata Oluştu')
    sys.exit()

def object_detection(frame,yolov7_detector):
    bbox ,scores, class_ids= yolov7_detector(frame)
    if bbox == []:
        bbox = False
        
        if bbox is not False :
            bbox = (bbox[0][0],bbox[0][1],bbox[0][2],bbox[0][3])
            bbox = (bbox[0],bbox[1],(bbox[2]-bbox[0]), (bbox[3]-bbox[1]))
        print(bbox)
        return bbox    
while True:
    ok, frame = video.read()
    
    detect = object_detection(frame,yolov7_detector)
    print(detect)






    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27: 
        break