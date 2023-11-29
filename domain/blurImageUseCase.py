from PIL import ImageFilter

class BlurImageUseCase:
    def execute(self, image, blur_radius):
        print("Radius to blur: ", blur_radius)
        return image.filter(ImageFilter.BoxBlur(blur_radius))
