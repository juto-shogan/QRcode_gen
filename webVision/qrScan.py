import cv2
from pyzbar.pyzbar import decode

# Initialize video capture object
cap = cv2.VideoCapture(0)  # Change to video file path if needed

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale (improves QR code detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Decode QR codes in the frame
    qrcodes = decode(gray)

    # Draw bounding boxes around detected QR codes (optional)
    for qrcode in qrcodes:
        (x, y, w, h) = qrcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract data from the QR code
        data = qrcode.data.decode("utf-8")
        print(f"QR Code Data: {data}")

        # Add text overlay with data (optional)
        cv2.putText(frame, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('QR Scanner', frame)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release capture object
cap.release()
cv2.destroyAllWindows()
