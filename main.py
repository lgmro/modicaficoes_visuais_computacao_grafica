from rotateImageUseCase import RotateImageUseCase
from translationImageUseCase import TranslationImageUseCase
from scaleImageUseCase import ScaleImageUseCase
from homeLayout import HomeLayout

def main():
    # Dependencies
    rotateImageUseCaseImpl = RotateImageUseCase()
    translationImageUseCaseImpl = TranslationImageUseCase()
    scaleImageUseCaseImpl = ScaleImageUseCase()

    HomeLayout(
        rotateImageUseCaseImpl, 
        translationImageUseCaseImpl, 
        scaleImageUseCaseImpl
        )
    
main()
