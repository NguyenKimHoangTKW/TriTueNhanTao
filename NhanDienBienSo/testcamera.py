import cv2
import pytesseract

cap = cv2.VideoCapture(0)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

while True:
    ret, frame = cap.read()
    # Resize the frame for better license plate detection
    frame = cv2.resize(frame, (640, 480))

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    nhungfilenhandien = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

    # Adjust the minSize parameter for specific size constraints (height: 165, length: 330)
    detections = nhungfilenhandien.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=5, minSize=(165, 80))

    for (x, y, w, h) in detections:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

        # Adjust the region of interest (ROI) based on specific size constraints
        number_plate = frame[y:y + h, x:x + w]

        gray = cv2.cvtColor(number_plate, cv2.COLOR_BGR2GRAY)
        custom_config = r'--oem 3 --psm 6 outputbase alphanumeric'
        plate_text = pytesseract.image_to_string(gray, config=custom_config)
        cv2.putText(frame, "Phat hien bien so: " + plate_text, (x - 10, y - 10),
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255), 2)
        cv2.imshow("Bien So Xe", gray)

    if cv2.waitKey(1) == ord('s'):
        break

    cv2.imshow("Bien so : ", frame)

cap.release()
cv2.destroyAllWindows()
