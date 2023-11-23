class RotateImageUseCase:
    async def execute(self, image, value):
        print("Angle to rotate", value)
        return image.rotate(value, expand=True)