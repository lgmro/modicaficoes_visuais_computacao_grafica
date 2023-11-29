from PIL import Image

class ScaleImageUseCase:
    def execute(self, image, value):
        original_image = image
        width, height = image.size
        print(f'O tamanho original da imagem é: {width}x{height}')
        scale_value = value / 100
        new_size = (int(width * scale_value), int(height * scale_value))
        scaled_image = original_image.resize(new_size, Image.LANCZOS)
        width, height = scaled_image.size
        print(f'O tamanho da imagem após a mudança de escala é: {width}x{height}')
        print(f'Redimensionado para: {value}%')
        return scaled_image
