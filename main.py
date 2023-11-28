from domain.rotateImageUseCase import RotateImageUseCase
from domain.translationImageUseCase import TranslationImageUseCase
from domain.scaleImageUseCase import ScaleImageUseCase
from domain.brightnessImageUseCase import BrightnessImageUseCase
from domain.blurImageUseCase import BlurImageUseCase
from presenter.homeLayout import HomeLayout
from presenter.homeViewModel import HomeViewModel

def main():
    # Dependencies
    rotate_image_use_case_impl = RotateImageUseCase()
    translation_image_use_case_impl = TranslationImageUseCase()
    scale_image_use_case_impl = ScaleImageUseCase()
    brightness_image_use_case_impl = BrightnessImageUseCase()
    blur_image_use_case_impl = BlurImageUseCase()

    home_view_model = HomeViewModel(
        rotate_image_use_case_impl,
        translation_image_use_case_impl,
        scale_image_use_case_impl,
        brightness_image_use_case_impl,
        blur_image_use_case_impl
    )

    HomeLayout(home_view_model)
    
main()
