import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time, os, sys

os.dup2(os.open(os.devnull, os.O_RDWR), sys.stderr.fileno())

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detected_qr_codes = {}

while cap.isOpened():
    ret, img = cap.read()
    if not ret: break

    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        if myData not in detected_qr_codes or (time.time() - detected_qr_codes[myData] > 5):
            print(myData)
            detected_qr_codes[myData] = time.time()

        pts = np.array([barcode.polygon], np.int32).reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        cv2.putText(img, myData, barcode.rect[:2], cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
