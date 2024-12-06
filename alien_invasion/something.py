from PIL import Image

image = Image.open("alien_invasion/images/disgustingcreature2.png")

new_size = (40,70)
resized_image = image.resize(new_size)

resized_image.save("alien_invasion/images/disgustingcreature.png")