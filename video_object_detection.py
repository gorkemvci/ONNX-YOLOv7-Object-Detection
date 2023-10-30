import cv2


from yolov7 import YOLOv7

# # Initialize video
# cap = cv2.VideoCapture("input.mp4")


# out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (1280, 720))

# Initialize YOLOv7 model
prev_frame_time = 0
new_frame_time = 0
model_path = "models/best.onnx"
yolov7_detector = YOLOv7(model_path, conf_thres=0.5, iou_thres=0.5)
cap = cv2.VideoCapture('uav.mp4')
cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
while cap.isOpened():

    # Press key q to stop
    if cv2.waitKey(1) == ord('q'):
        break

    try:
        # Read frame from the video
        ret, frame = cap.read()
        if not ret:
            break
    except Exception as e:
        print(e)
        continue

    # Update object localizer
    boxes, scores, class_ids = yolov7_detector(frame)

    combined_img = yolov7_detector.draw_detections(frame)
    cv2.imshow("Detected Objects", combined_img)
    # out.write(combined_img)

# out.release()
