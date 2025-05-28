```markdown
# QR Code Generator and Scanner

This repository contains two simple Python scripts: one for generating QR codes from user input and another for scanning QR codes using a webcam.

## Features

* **`qrGen.py`**: Generates a QR code from user-provided text and saves it as a PNG image.
* **`qrScan.py`**: Utilises your webcam to detect and decode QR codes in real-time. It displays the decoded data on the screen.

## Prerequisites

You will need to install Python on your system to run these scripts.
You will also need the following Python libraries:

* `qrcode`
* `opencv-python` (OpenCV)
* `pyzbar`

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/juto-shogan/QRcode_gen.git](https://github.com/juto-shogan/QRcode_gen.git)
    cd QRcode_gen
    ```

2.  **Install the required Python libraries:**
    It's recommended to use a virtual environment.

    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate the virtual environment
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate

    # Install the libraries
    pip install qrcode opencv-python pyzbar
    ```

## Usage

### Generating a QR Code

To generate a QR code, run the `qrGen.py` script:

```bash
python qrGen.py
```

The script will prompt you to "Enter the data you want to encode in the QR code:". After entering your text, a QR code image named `qr_code.png` will be saved in the same directory.

### Scanning a QR Code

To scan QR codes using your webcam, run the `qrScan.py` script:

```bash
python qrScan.py
```
