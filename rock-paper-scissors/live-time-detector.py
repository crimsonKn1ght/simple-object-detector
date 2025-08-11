import cv2
from ultralytics import YOLO

from config import model_path, conf_thres, imgsz, device


model = YOLO(model_path)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

last_label = None

model.overrides["verbose"] = False

window_name = "YOLO11 - press q or ESC to quit"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

try:
    while True:
        ok, frame = cap.read()
        if not ok:
            break

        results = model(frame, conf=conf_thres, imgsz=imgsz, device=device, verbose=False)
        r = results[0]

        if len(r.boxes) > 0:
            i = int(r.boxes.conf.argmax())
            cls_id = int(r.boxes.cls[i])
            label = r.names.get(cls_id, str(cls_id))
        else:
            label = "none"

        if label != last_label:
            print(label)
            last_label = label

        annotated = r.plot()
        cv2.imshow(window_name, annotated)

        key = cv2.waitKey(1) & 0xFF
        if key in (27, ord('q')):
            break
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
