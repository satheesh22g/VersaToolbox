from PIL import Image

def test_pillow_open_image():
    img = Image.new('RGB', (100, 100), color='red')
    assert img.size == (100, 100)  # Check if the image size is correct

def test_pillow_convert_to_grayscale():
    img = Image.new('RGB', (100, 100), color='blue')
    gray_img = img.convert('L')
    assert gray_img.mode == 'L'  # Check if the image is converted to grayscale
