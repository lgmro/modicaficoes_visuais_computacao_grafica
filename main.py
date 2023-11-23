from rotateImageUseCase import RotateImageUseCase
from translationImageUseCase import TranslationImageUseCase
from scaleImageUseCase import ScaleImageUseCase
from homeLayout import HomeLayout
from homeViewModel import HomeViewModel

def main():
    # Dependencies
    rotateImageUseCaseImpl = RotateImageUseCase()
    translationImageUseCaseImpl = TranslationImageUseCase()
    scaleImageUseCaseImpl = ScaleImageUseCase()

    home_view_model = HomeViewModel(
        rotateImageUseCaseImpl,
        translationImageUseCaseImpl,
        scaleImageUseCaseImpl
    )

    HomeLayout(home_view_model)
    
main()
