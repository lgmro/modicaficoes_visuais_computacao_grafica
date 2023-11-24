from rotateImageUseCase import RotateImageUseCase
from translationImageUseCase import TranslationImageUseCase
from scaleImageUseCase import ScaleImageUseCase
from brightnessUseCase import BrightnessUseCase
from homeLayout import HomeLayout
from homeViewModel import HomeViewModel

def main():
    # Dependencies
    rotateImageUseCaseImpl = RotateImageUseCase()
    translationImageUseCaseImpl = TranslationImageUseCase()
    scaleImageUseCaseImpl = ScaleImageUseCase()
    brightnessUseCaseImpl = BrightnessUseCase()

    home_view_model = HomeViewModel(
        rotateImageUseCaseImpl,
        translationImageUseCaseImpl,
        scaleImageUseCaseImpl,
        brightnessUseCaseImpl
    )

    HomeLayout(home_view_model)
    
main()
