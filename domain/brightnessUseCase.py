from PIL import ImageEnhance

class BrightnessUseCase:
    async def execute(self, image, value):
        if value > 0:
            print("Brilho: ", value)
            image = ImageEnhance.Brightness(image)
            image = image.enhance(value)
        return image