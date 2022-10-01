from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save('sharp.png', 'png')

filtered_img = img.convert('L')
# crooked_img = filtered_img.rotate(90)
# crooked_img.save('crooked.png', 'png')
# filtered_img.show()
# resized_img = filtered_img.resize((300, 300))
# resized_img.save('resized.png', 'png')
box = (100, 100, 400, 400)
cropped_img = filtered_img.crop(box)
cropped_img.save('cropped.png', 'png')