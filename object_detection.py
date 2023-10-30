import cv2
import time
from yolov7 import YOLOv7

# Initialize the webcam
frame = cv2.VideoCapture('UAV_Examples/uav1.jpg')

# Initialize YOLOv7 object detector
model_path = "models/best.onnx"

yolov7_detector = YOLOv7(model_path, conf_thres=0.5, iou_thres=0.5)
#cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
boxes, scores, class_ids = yolov7_detector(frame)
combined_img = yolov7_detector.draw_detections(frame)
cv2.imshow("Detected Objects", combined_img)

# cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
# while True:

#     # Read frame from the video
#     ret, frame = cap.read()

#     if not ret:
#         break
#     time.sleep(6)
#     # Update object localizer
#     boxes, scores, class_ids = yolov7_detector(frame)

#     combined_img = yolov7_detector.draw_detections(frame)
#     cv2.imshow("Detected Objects", combined_img)
   
#     # Press key q to stop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
