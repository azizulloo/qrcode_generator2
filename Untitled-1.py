import qrcode
import random
import string


link = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

file_name = ''.join(random.choices(string.ascii_lowercase, k=8)) + '.png'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

qr.make_image(fill_color="black", back_color="white").save(file_name)

print(f"Generated QR code for link: {link}")
print(f"Saved as: {file_name}")
