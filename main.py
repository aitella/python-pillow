# response = ['li[id=bundle-239]', 'li[id=bundle-96]', 'li[id=bundle-200]', 'li[id=bundle-98]', 'li[id=bundle-174]', 'li[id=bundle-192]', 'li[id=bundle-173]', 'li[id=bundle-72]'];
# for i in response:
#     print (i);

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter

def imgfu(img):
    original = Image.open(img)
    flag = Image.open('in.png')
    original.load()
    draw = ImageDraw.Draw(original)
    area = (20, 35)
    original.paste(flag, area)
    # fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
    font1 = ImageFont.truetype("HELR45W.ttf", 16)
    font2 = ImageFont.truetype("HELR45W.ttf", 22)
    font3 = ImageFont.truetype("HELR45W.ttf", 13)
    # ImageFont.load_path(file)
    # font = ImageFont.load("sans-serif.pil")
    # font = ImageFont.load_default()
    # font2 = ImageFont.load_default()
    draw.text((52, 10), "India Unlimited", (6, 0, 0), font = font1)
    draw.text((95, 45), "$14.95", (6, 0, 0), font = font2)
    draw.text((40, 90), "Landline and Mobile", (109, 109, 120), font = font3)
    original.save("fufufu.png")
    # print(original.format, original.size, original.mode)
    # original.point(lambda i: i * 1.2)

imgfu("myimg.png")
