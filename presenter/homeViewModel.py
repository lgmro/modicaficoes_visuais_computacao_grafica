import os
from PIL import Image
from presenter.utils.event import post_event, post_event_async
from domain.rotateImageUseCase import RotateImageUseCase
from domain.translationImageUseCase import TranslationImageUseCase
from domain.scaleImageUseCase import ScaleImageUseCase
from domain.brightnessImageUseCase import BrightnessImageUseCase
from domain.blurImageUseCase import BlurImageUseCase
from presenter.utils.logger import Logger

class HomeViewModel:
    def __init__(
            self, rotate_image_use_case: RotateImageUseCase, 
            translation_image_use_case: TranslationImageUseCase, 
            scale_image_use_case: ScaleImageUseCase, 
            brighten_image_use_case: BrightnessImageUseCase,
            blur_image_use_case: BlurImageUseCase,
            logger: Logger
            ):
        self.rotate_image_use_case = rotate_image_use_case 
        self.translation_image_use_case = translation_image_use_case 
        self.scale_image_use_case = scale_image_use_case
        self.brighten_image_use_case = brighten_image_use_case
        self.blur_image_use_case = blur_image_use_case
        self.logger = logger
        self.image_modified = None
        self.image_default = None
        self.image_path = ""
        self.location_save_image = ""
        self.input_from_dialog = ""
    
    async def update_path(self, value):
        self.image_path = value
        self.logger.info(f"Update image path variable: {self.image_path}")
    
    async def update_location_save_image(self, value):
        self.location_save_image = value
        self.logger.info(f"Update location to save image: {self.location_save_image}")
    
    async def update_input_from_dialog(self, value):
        self.input_from_dialog = value
    
    async def save_image_on_location(self):
        try:
            self.image_modified.save(os.path.join(self.location_save_image))
        except ValueError:
            self.logger.info("Save operation canceled.")
        except:
            self.logger.info("Unexpected error.")
    
    async def first_load_image_on_labels(self):
        try:
            self.image_default = Image.open(os.path.join(self.image_path))
            self.image_modified = self.image_default
            post_event("update_image_transformed_label", self.image_modified)
        except TypeError:
            self.logger.info("Any image selected.")
        except IOError:
            self.logger.info("Your file is not a image.")
        except:
            self.logger.info("Unexpected error.")
    
    async def reset_image_to_default(self):
        self.image_modified = self.image_default
        post_event("update_image_transformed_label", self.image_modified)
    
    async def rotate_image(self, value):
        self.image_modified = await self.rotate_image_use_case.execute(self.image_modified, value)
        post_event("update_image_transformed_label", self.image_modified)
    
    async def translation_image(self): 
        await post_event_async("get_input_from_dialog", "Informe valor para a translação no eixo X")
        value_axle_x = self.input_from_dialog
        await post_event_async("get_input_from_dialog", "Informe valor para a translação no eixo Y")
        value_axle_y = self.input_from_dialog
        
        self.image_modified = self.translation_image_use_case.execute(self.image_modified, float(value_axle_x), float(value_axle_y))
        post_event("update_image_transformed_label", self.image_modified)
    
    async def scale_image(self):
        await post_event_async("get_input_from_dialog", "Informe valor para a escala")
        self.image_modified = self.scale_image_use_case.execute(self.image_modified, int(self.input_from_dialog))
        post_event("update_image_transformed_label", self.image_modified)

    async def brighten_image(self, value):
        self.image_modified = await self.brighten_image_use_case.execute(self.image_modified, int(value))
        post_event("update_image_transformed_label", self.image_modified)
    
    async def blur_image(self):
        await post_event_async("get_input_from_dialog", "Informe o valor do radius")
        self.image_modified = self.blur_image_use_case.execute(self.image_modified, float(self.input_from_dialog))
        post_event("update_image_transformed_label", self.image_modified)
