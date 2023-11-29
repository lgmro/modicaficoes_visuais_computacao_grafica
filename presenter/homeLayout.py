import customtkinter
import os
from tkinter import filedialog
import platform
import asyncio
from presenter.utils.event import subscribe
from presenter.utils.logger import Logger
from presenter.homeViewModel import HomeViewModel

class HomeLayout:
    def __init__(self, home_view_model: HomeViewModel, logger: Logger):
        # Variables
        global root
        self.view_model = home_view_model
        self.logger = logger
        self.weight = 600
        self.height = 500 

        # System information
        self.logger.info(f"System: {platform.system()}")

        # Creating root
        root = customtkinter.CTk()
        root.geometry(f"{1300}x{800}")
        root.title("Modificações Visuais em Imagem")

        # configure grid layout (4x4)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure((2, 3), weight=0)
        root.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebars frame with widgets
        self.create_sidebars()

        # Buttons
        self.create_buttons()

        # Sliders
        self.create_slide_brightness()
        self.create_slide_rotate()

        # Settings of app
        self.create_settings_app()

        # Label to display image
        self.create_label_to_display_image()

        # Register events
        self.subscribe_events()

        root.mainloop()

    def subscribe_events(self):
        subscribe("update_image_transformed_label", self.update_image_modify_on_label)
        subscribe("get_input_from_dialog", self.open_input_dialog_event)

    def create_sidebars(self):
        self.sidebar_frame = customtkinter.CTkFrame(root, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Opções", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_bottom_frame = customtkinter.CTkFrame(root, corner_radius=0)
        self.sidebar_bottom_frame.grid(row=3, column=1, sticky="nsew")
        self.sidebar_bottom_frame.grid_columnconfigure(5, weight=1)

    def create_buttons(self):
        self.button_open_image = customtkinter.CTkButton(self.sidebar_frame, command=lambda: asyncio.run(self.open_image()), text="Abrir Imagem")
        self.button_open_image.grid(row=1, column=0, padx=20, pady=10)

        self.button_translation = customtkinter.CTkButton(self.sidebar_frame, text="Translação", command=lambda: asyncio.run(self.view_model.translation_image()))
        self.button_translation.grid(row=2, column=0, padx=20, pady=10)

        self.button_scale = customtkinter.CTkButton(self.sidebar_frame, text="Escala", command=lambda: asyncio.run(self.view_model.scale_image()))
        self.button_scale.grid(row=3, column=0, padx=20, pady=10)

        self.button_blur = customtkinter.CTkButton(self.sidebar_frame, text="Blur", command=lambda: asyncio.run(self.view_model.blur_image()))
        self.button_blur.grid(row=4, column=0, padx=20, pady=10)

        self.button_reset = customtkinter.CTkButton(master=self.sidebar_bottom_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Resetar", command=lambda: asyncio.run(self.view_model.reset_image_to_default()))
        self.button_reset.grid(row=1, column=6, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.button_save = customtkinter.CTkButton(master=self.sidebar_bottom_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Salvar", command=lambda: asyncio.run(self.save_image()))
        self.button_save.grid(row=2, column=6, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # set default values
        self.button_translation.configure(state="disabled")
        self.button_scale.configure(state="disabled")
        self.button_blur.configure(state="disabled")
        self.button_reset.configure(state="disabled")
        self.button_save.configure(state="disabled")

    def slide_event_brightness(self, value):
        asyncio.run(self.view_model.brighten_image(value))
        self.label_brightness_value.configure(text=int(value))
    
    def slide_event_rotate(self, value):
        asyncio.run(self.view_model.rotate_image(value))
        self.label_rotate_value.configure(text=int(value)) 

    def create_slide_rotate(self):
        self.label_slide_name_rotate = customtkinter.CTkLabel(master=self.sidebar_bottom_frame, text="Rotação", width=60, height=25, text_color=("white"))
        self.label_slide_name_rotate.grid(row=2, column=1, padx=20, pady=10)

        self.slider_rotate = customtkinter.CTkSlider(master=self.sidebar_bottom_frame, from_=-360, to=360, number_of_steps=8, command=self.slide_event_rotate)
        self.slider_rotate.grid(row=2, column=2, padx=(20, 10), pady=(10, 10), sticky="ew")

        self.label_rotate_value = customtkinter.CTkLabel(master=self.sidebar_bottom_frame, text="0", width=60, height=25, fg_color=("black"), text_color=("white"))
        self.label_rotate_value.grid(row=2, column=3, padx=20, pady=10)

        # Default values
        self.slider_rotate.set(0)
        self.slider_rotate.configure(state="disabled")
         
    def create_slide_brightness(self):
        self.label_slide_name_brightness = customtkinter.CTkLabel(master=self.sidebar_bottom_frame, text="Brilho", width=60, height=25, text_color=("white"))
        self.label_slide_name_brightness.grid(row=1, column=1, padx=20, pady=10)

        self.slider_brightness = customtkinter.CTkSlider(master=self.sidebar_bottom_frame, from_=0, to=5, number_of_steps=5, command=self.slide_event_brightness, width=500)
        self.slider_brightness.grid(row=1, column=2, padx=(20, 10), pady=(10, 10), sticky="ew")

        self.label_brightness_value = customtkinter.CTkLabel(master=self.sidebar_bottom_frame, text="0", width=60, height=25, fg_color=("black"), text_color=("white"))
        self.label_brightness_value.grid(row=1, column=3, padx=20, pady=10)

        # Default values
        self.slider_brightness.set(0)
        self.slider_brightness.configure(state="disabled")

    def create_settings_app(self):
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Aparência:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Escala do aplicativo:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

    def create_label_to_display_image(self):
        self.image_modify_label = customtkinter.CTkLabel(root, text="")
        self.image_modify_label.grid(row=0, column=1, columnspan = 2, padx=(20, 0), pady=(20, 0))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    async def open_image(self):
        start = os.path.expanduser('~') + "/Pictures"
        self.logger.info(f"Location dialog opened: {start}")

        img_path = filedialog.askopenfilename(
            initialdir=start,
            title="Select a image",
            filetypes=(('PNG files', '*.png'), ("jpeg files", "*.jpeg"), ('JPG files', '*.jpg'), ('JPEG files', '*.jpeg'), ("all files", "*.*"))
        )

        await self.view_model.update_path(img_path)
        await self.view_model.first_load_image_on_labels()

        self.enable_buttons_sliders()

    def enable_buttons_sliders(self):
        self.button_translation.configure(state="enable")
        self.button_scale.configure(state="enable")
        self.button_blur.configure(state="enable")
        self.button_reset.configure(state="enable")
        self.button_save.configure(state="enable")
        self.slider_brightness.configure(state="normal")
        self.slider_rotate.configure(state="normal")

    def update_image_modify_on_label(self, image_update):
        image = customtkinter.CTkImage(image_update, size=(self.weight, self.height))
        self.image_modify_label.configure(image = image)

    async def save_image(self):
        location = filedialog.asksaveasfilename(defaultextension=".png")

        await self.view_model.update_location_save_image(location)
        await self.view_model.save_image_on_location()
        
        if location:
            self.logger.info(f"Image saved on: {location}")

    async def open_input_dialog_event(self, text_dialog_input):
        await self.view_model.update_input_from_dialog(customtkinter.CTkInputDialog(text=text_dialog_input, title="").get_input()) 
