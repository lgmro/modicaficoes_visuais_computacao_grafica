from domain.rotateImageUseCase import RotateImageUseCase
from domain.translationImageUseCase import TranslationImageUseCase
from domain.scaleImageUseCase import ScaleImageUseCase
from domain.brightnessImageUseCase import BrightnessImageUseCase
from domain.blurImageUseCase import BlurImageUseCase
from presenter.homeLayout import HomeLayout
from presenter.homeViewModel import HomeViewModel
from presenter.utils.logger import Logger

def main():
    # Dependencies
    logger = Logger()
    rotate_image_use_case_impl = RotateImageUseCase(logger)
    translation_image_use_case_impl = TranslationImageUseCase(logger)
    scale_image_use_case_impl = ScaleImageUseCase(logger)
    brightness_image_use_case_impl = BrightnessImageUseCase(logger)
    blur_image_use_case_impl = BlurImageUseCase(logger)

    home_view_model = HomeViewModel(
        rotate_image_use_case_impl,
        translation_image_use_case_impl,
        scale_image_use_case_impl,
        brightness_image_use_case_impl,
        blur_image_use_case_impl,
        logger
    )

    HomeLayout(home_view_model, logger)
    
main()
