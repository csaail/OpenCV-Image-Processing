import cv2, time

cap = cv2.VideoCapture(0)
last_print_time, last_color = time.time(), None

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width = frame.shape[:2]
    cx, cy = width // 2, height // 2
    hue_value = hsv_frame[cy, cx][0]

    color = ("RED" if hue_value < 5 or hue_value >= 167 else
             "ORANGE" if hue_value < 22 else
             "YELLOW" if hue_value < 33 else
             "GREEN" if hue_value < 78 else
             "BLUE" if hue_value < 131 else
             "VIOLET")

    if color in ["RED", "YELLOW", "BLUE"] and color != last_color:
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Detected color: {color}")
        last_print_time, last_color = time.time(), color

    b, g, r = map(int, frame[cy, cx])
    cv2.putText(frame, color, (10, 70), 0, 1.5, (b, g, r), 2)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
