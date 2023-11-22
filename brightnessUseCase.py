from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps

class brightnessUseCase:
    def execute(self, image, value):
        print(image)

        newImage = Image.open(image)
        newImage = ImageEnhance.Brightness(newImage)
        newImage = newImage.enhance(int(value))

        print(newImage)
        print("oi")
        return newImage
    


# global img_path, img2, img3
#     for m in range(0, v2.get()+1):
#         img = Image.open(image)
#         img.thumbnail((350, 350))
#         imgg = ImageEnhance.Brightness(img)
#         img2 = imgg.enhance(m)
#         img3 = ImageTk.PhotoImage(img2)
#         canvas2.create_image(300, 210, image=img3)
#         canvas2.image = img3