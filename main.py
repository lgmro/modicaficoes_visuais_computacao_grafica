from domain.rotateImageUseCase import RotateImageUseCase
from domain.translationImageUseCase import TranslationImageUseCase
from domain.scaleImageUseCase import ScaleImageUseCase
from domain.brightnessUseCase import BrightnessUseCase
from presenter.homeLayout import HomeLayout
from presenter.homeViewModel import HomeViewModel

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
