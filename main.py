from rotateImageUseCase import RotateImageUseCase
from translationImageUseCase import TranslationImageUseCase
from scaleImageUseCase import ScaleImageUseCase
from brightnessUseCase import brightnessUseCase
from homeLayout import HomeLayout


def main():
    # Dependencies
    rotateImageUseCaseImpl = RotateImageUseCase()
    translationImageUseCaseImpl = TranslationImageUseCase()
    scaleImageUseCaseImpl = ScaleImageUseCase()
    brightnessUseCaseImpl = brightnessUseCase()

    HomeLayout(
        rotateImageUseCaseImpl, 
        translationImageUseCaseImpl, 
        scaleImageUseCaseImpl,
        brightnessUseCaseImpl
        )
    
main()
