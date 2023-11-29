from PIL import ImageFilter
from presenter.utils.logger import Logger

class BlurImageUseCase():
    def __init__(self, logger: Logger):
        self.logger = logger
        
    def execute(self, image, blur_radius):
        if (blur_radius < 0):
            self.logger.info(f"Don't use negative value: {blur_radius}")
            return image
        
        self.logger.info(f"Radius to blur: {blur_radius}")
        return image.filter(ImageFilter.BoxBlur(blur_radius))
