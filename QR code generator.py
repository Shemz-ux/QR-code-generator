import qrcode
import os

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

def convertUrl():
    url = input("Please insert url here: ")
    qr.add_data(url)
    qr.make(fit = True)

    img = qr.make_image(fill_color ="black", back_color="white")

    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    file_path = os.path.join(downloads_folder, "QrCode.png")
    img.save(file_path)

    print("QR code has been created successfully! Check downloads folder.")

def main():
    print("This a QR code generator created by Shemz-ux version 1.0.0")

    convertUrl()

if __name__ == "__main__":
    main()

# helllo world






