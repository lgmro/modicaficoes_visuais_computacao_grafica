from presenter.utils.logger import Logger

class RotateImageUseCase:
    def __init__(self, logger: Logger):
        self.logger = logger

    async def execute(self, image, value):
        self.logger.info(f"Angle to rotate: {value}")
        return image.rotate(value, expand=True)