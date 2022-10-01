from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save('sharp.png', 'png')

filtered_img = img.convert('L')
filtered_img.save('gray.png', 'png')