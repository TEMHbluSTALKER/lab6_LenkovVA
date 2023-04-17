import re
import random
import time
#Функции
###################################################
def TaskSelection():
    print("Выберите номер задачи:\n"
          "1 - Информация о фото.\n"
          "2 - Уменьшить изображение в 3 раза.\n"
          "3 - Фильтры на изображение.\n"
          "4 - Водяной знак.")
    number = input()
    match number:
        case "1":
            PhotoInformation()
        case "2":
            ReduceTheImageBy3Times()
        case "3":
            FilterOnImages()
        case "4":
            Watermark()
        case _:
            print("Введен неправильный номер.")
            TaskSelection()

###################################################
def PhotoInformation():
    from PIL import Image
    filename = "car.jpeg"
    with Image.open(filename) as img:
        img.load()
        img.show()
    width, height = img.size
    format = img.format
    mode = img.mode
    print("Ширина: ", width)
    print("Высота:  ", height)
    print("Формат: ", format)
    print("Цветовая модель:", mode)
###################################################

def ReduceTheImageBy3Times():
    from PIL import Image
    filename = "car.jpeg"
    with Image.open(filename) as img:
        img.load()
    new_img = img.resize((img.width // 3, img.height // 3))
    new_img.save("image_reduced.jpeg")
    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img.save("image_flip_hor.jpeg")
    converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    converted_img.save("image_flip_vert.jpeg")
###################################################

def FilterOnImages():
    from PIL import Image, ImageFilter
    filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.FIND_EDGES)
            # new_img.show()
            new_img.save("new_" + file)
###################################################

def Watermark():
    from PIL import Image
    water = "watermark.png"
    with Image.open(water) as img_water:
        img_water.load()
    img_water = Image.open(water)
    img_water = img_water.resize((img_water.width // 4, img_water.height // 4))
    filename = "car.jpeg"
    with Image.open(filename) as img:
        img.load()
    img.paste(img_water, (20, 550), img_water)
    img.save("watermark_image.jpg")
###################################################

#Основная программа
TaskSelection()
