import qrcode

def test_qrcode_generation():
    # Generate a simple QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data('https://www.example.com')
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    assert img.size[0] > 0 and img.size[1] > 0  # Ensure the image has valid size
