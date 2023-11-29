from PIL import ImageEnhance
from presenter.utils.logger import Logger

class BrightnessImageUseCase:
    def __init__(self, logger: Logger):
        self.logger = logger

    async def execute(self, image, value):
        if value > 0:
            self.logger.info(f"Brilho: {value}")
            image = ImageEnhance.Brightness(image)
            image = image.enhance(value)
        return image