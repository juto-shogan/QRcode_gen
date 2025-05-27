import qrcode

# User input for data to encode
data = input("Enter the data you want to encode in the QR code: ")

# Create a QR code object with error correction level (optional)
qr = qrcode.QRCode(
    version=1,  # Adjust version for size and data capacity
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Choose error correction level
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)  # Fit data to QR code size

# Create an image from the QR code data
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("qr_code.png")

print("QR code generated and saved as qr_code.png")
