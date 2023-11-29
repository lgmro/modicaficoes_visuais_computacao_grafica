from PIL import Image
from presenter.utils.logger import Logger

class ScaleImageUseCase:
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, image, value):
        if (value < 0):
            self.logger.info(f"Don't use negative value: {value}")
            return image
        
        original_image = image
        width, height = image.size
        self.logger.info(f'The original size of image is: Width: {width} x Height: {height}')

        scale_value = value / 100
        new_size = (int(width * scale_value), int(height * scale_value))
        scaled_image = original_image.resize(new_size, Image.LANCZOS)
        width, height = scaled_image.size

        self.logger.info(f'The size of image after scale is: Width: {width} x Height: {height}')
        self.logger.info(f'Resized to: {value}%')

        return scaled_image