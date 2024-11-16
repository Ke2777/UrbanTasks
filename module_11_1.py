from PIL import Image, ImageFilter, ImageDraw, ImageFont

image = Image.open("module_11_1_res/example.jpg")
print(f"Оригинальный размер: {image.size}")

resized_image = image.resize((200, 200))
resized_image.save("module_11_1_res/resized_image.jpg")

rotated_image = image.rotate(45)
rotated_image.save("module_11_1_res/rotated_image.jpg")

blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save("module_11_1_res/blurred_image.jpg")

resized_image.show()
rotated_image.show()
blurred_image.show()

