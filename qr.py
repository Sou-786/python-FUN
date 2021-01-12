import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://medium.com/@soumitkar.5/kaplan-meier-curve-6319a978c451')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('advanced.png')