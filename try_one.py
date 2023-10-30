import cv2
import sys
from yolov7 import YOLOv7
import time
model_path = "models/yolov7.onnx"
count=0
refresh = 0
object_detection = False
object_tracking = False
object_tracking_statues = "Waiting-Detect"
yolov7_detector = YOLOv7(model_path, conf_thres=0.5, iou_thres=0.5)
video = cv2.VideoCapture('UAV_Examples/uav1.mp4')
prev_frame_time = 0
new_frame_time = 0
if not video.isOpened():
    print('Bir Hata Oluştu')
    sys.exit()
while True:
    new_frame_time = time.time()
    ok, frame = video.read()
    frameshape = frame.shape
   
    height = int(frameshape[0])
    width = int(frameshape[1])
    
    if object_detection == False:
        boxes ,scores, class_ids=yolov7_detector(frame)
        if boxes != [] :
            tracker = cv2.legacy.TrackerCSRT_create()
            object_detection = True
            bbox = (boxes[0][0],boxes[0][1],boxes[0][2],boxes[0][3])
            bbox = (bbox[0],bbox[1],(bbox[2]-bbox[0]), (bbox[3]-bbox[1]))
            ok = tracker.init(frame, bbox)
            start_time = time.time()
        
    if object_detection == True: 
        ok, bbox = tracker.update(frame)
        if ok == True:
            object_tracking_statues = "Success"
            (x, y, w, h) = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,0), 3)
            line_x =int((2*x+w)/2)
            line_y = int((2*y+h)/2)
            cv2.line(frame, (640,360), (line_x,line_y), (255,0, 0),2)
            stop_time = time.time()
            count =stop_time - start_time
            if count > 4:
                refresh = refresh + 1
                object_tracking_statues = "Waiting-Detect"
                object_detection = False
                bbox = []
        else:
            object_detection = False
            bbox = []
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
     # converting the fps into integer
    fps = int(fps)
  
    # converting the fps to string so that we can display it on frame
    # by using putText function
  
    # putting the FPS count on the frame
    str_count = round(count,2)
    cv2.putText(frame,f"Tracking-Statues: {object_tracking_statues} ", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255),2, cv2.LINE_AA)
    cv2.putText(frame,f"Tracking-Time: {str_count}",(10,80), cv2.FONT_HERSHEY_SIMPLEX , 0.75,(0,0,255),2, cv2.LINE_AA)
    cv2.putText(frame,f"Detect - Refresh: {refresh}",(10,110), cv2.FONT_HERSHEY_SIMPLEX , 0.75,(0,0,255),2, cv2.LINE_AA)
    cv2.putText(frame,f"Tracking - Process: {refresh*4}",(10,140), cv2.FONT_HERSHEY_SIMPLEX , 0.75,(0,0,255),2, cv2.LINE_AA)
    cv2.line(frame, (640,380), (640,340), (0,255, 0),5)
    cv2.line(frame, (660,360), (620,360), (0,255, 0),5)
    
    cv2.rectangle(frame, (320, 72), (960,648) , (0,255, 0), 3)
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0XFF == 27: # esc
        break