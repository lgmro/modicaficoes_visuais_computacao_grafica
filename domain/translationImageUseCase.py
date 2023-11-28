from presenter.utils.logger import Logger

class TranslationImageUseCase:
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, image, value):
        newImage = image
        self.logger.info(f"Translation: {value}")
        return newImage