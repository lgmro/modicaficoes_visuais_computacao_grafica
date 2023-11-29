from presenter.utils.logger import Logger

class ScaleImageUseCase:
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, image, value):
        newImage = image
        self.logger.info(f"Scale: {value}")
        return newImage