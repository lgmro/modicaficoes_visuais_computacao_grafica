from PIL import ImageEnhance

class BrightnessUseCase:
    async def execute(self, image, value):
        print("Brilho: ", value)
        image = ImageEnhance.Brightness(image)
        image = image.enhance(value)
        
        return image