import tesserocr
from PIL import Image

image = Image.open('img_2.png')
gray_image = image.convert('L')
threshold = 150
table =[]

for i in range(256):
    if i < threshold:
        table.append(255)
    else:
        table.append(0)
out_image =gray_image.point(table, '1')
out_image.show()
result = tesserocr.image_to_text(out_image)
print(result)