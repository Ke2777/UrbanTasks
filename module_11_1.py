from PIL import Image, ImageFilter, ImageDraw, ImageFont
import numpy as np

# Загрузка изображения
image = Image.open("module_11_1_res/example.jpg")
print(f"Оригинальный размер: {image.size}")

# Изменение размера
resized_image = image.resize((200, 200))
resized_image.save("module_11_1_res/resized_image.jpg")

# Поворот изображения
rotated_image = image.rotate(45)
rotated_image.save("module_11_1_res/rotated_image.jpg")

# Размытие изображения
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save("module_11_1_res/blurred_image.jpg")

# Преобразование изображения в массив numpy
image_array = np.array(image)

# Инверсия цветов
inverted_image_array = 255 - image_array
inverted_image = Image.fromarray(inverted_image_array)
inverted_image.save("module_11_1_res/inverted_image.jpg")

brightened_image_array = np.clip(image_array + 50, 0, 255)
brightened_image = Image.fromarray(brightened_image_array.astype('uint8'))
brightened_image.save("module_11_1_res/brightened_image.jpg")

# Отображение результатов
resized_image.show()
rotated_image.show()
blurred_image.show()
inverted_image.show()
brightened_image.show()
