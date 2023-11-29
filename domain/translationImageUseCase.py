from presenter.utils.logger import Logger
from PIL import Image
import cv2
import numpy as np

class TranslationImageUseCase:
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, image, value_x, value_y):
        # Convert to numpy array and opencv image
        numpy_image = np.array(image)
        opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
        
        height, width = opencv_image.shape[:2]
        T = np.float32([[1, 0, value_x], [0, 1, value_y]]) 
        image_translation = cv2.warpAffine(opencv_image, T, (width, height))

        self.logger.info(f"Translation: Axle X: {value_x}, Axle Y: {value_y}")

        image_color_converted = cv2.cvtColor(image_translation, cv2.COLOR_BGR2RGB)
        return Image.fromarray(image_color_converted)