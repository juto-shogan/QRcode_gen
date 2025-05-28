```markdown
# QR Code Generator and Scanner

This repository contains two simple Python scripts: one for generating QR codes from user input and another for scanning QR codes using a webcam.

## Features

* **`qrGen.py`**: Generates a QR code from user-provided text and saves it as a PNG image.
* **`qrScan.py`**: Utilises your webcam to detect and decode QR codes in real-time. It displays the decoded data on the screen.

## Prerequisites
You will also need the following Python libraries:

* `qrcode`
* `opencv-python` (OpenCV)
* `pyzbar`

## Usage

### Generating a QR Code

To generate a QR code, run the `qrGen.py` script:
```
```bash
python qrGen.py
```

The script will prompt you to "Enter the data you want to encode in the QR code:". After entering your text, a QR code image named `qr_code.png` will be saved in the same directory.

### Scanning a QR Code

To scan QR codes using your webcam, run the `qrScan.py` script:

```bash
python qrScan.py
```
