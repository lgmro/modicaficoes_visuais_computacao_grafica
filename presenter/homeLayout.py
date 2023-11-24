import customtkinter
import os
from tkinter import filedialog
import platform
import asyncio
from presenter.utils.event import subscribe
from presenter.homeViewModel import HomeViewModel

class HomeLayout:
    def __init__(self, home_view_model: HomeViewModel):
        print(platform.system())
        print(os.path.expanduser('~'))

        # Variables
        global root
        self.view_model = home_view_model
        self.weight = 600
        self.height = 500

        # Creating root
        root = customtkinter.CTk()
        root.geometry(f"{1300}x{580}")
        root.title("Modificações Visuais em Imagem")

        # configure grid layout (4x4)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure((2, 3), weight=0)
        root.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.create_sidebar()

        # Buttons
        self.create_buttons()

        # Settings of app
        self.create_settings_app()

        # Labels to display image
        self.create_labels_to_display_images()

        self.subscribe_events()

        root.mainloop()

    def subscribe_events(self):
        subscribe("update_image_transformed_label", self.update_image_modify_on_label)
        subscribe("update_image_original_label", self.update_image_original_on_label)
        subscribe("get_input_from_dialog", self.open_input_dialog_event)

    def create_sidebar(self):
        self.sidebar_frame = customtkinter.CTkFrame(root, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Opções", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    def create_buttons(self):
        self.button_open_image = customtkinter.CTkButton(self.sidebar_frame, command=lambda: asyncio.run(self.open_image()), text="Abrir Imagem")
        self.button_open_image.grid(row=1, column=0, padx=20, pady=10)

        self.button_rotate = customtkinter.CTkButton(self.sidebar_frame, text="Rotacionar", command=lambda: asyncio.run(self.view_model.rotate_image()))
        self.button_rotate.grid(row=2, column=0, padx=20, pady=10)

        self.button_translation = customtkinter.CTkButton(self.sidebar_frame, text="Translação", command=lambda: asyncio.run(self.view_model.translation_image()))
        self.button_translation.grid(row=3, column=0, padx=20, pady=10)

        self.button_scale = customtkinter.CTkButton(self.sidebar_frame, text="Escala", command=lambda: asyncio.run(self.view_model.scale_image()))
        self.button_scale.grid(row=4, column=0, padx=20, pady=10)

        self.button_bright = customtkinter.CTkButton(self.sidebar_frame, text="Brilho", command=lambda: asyncio.run(self.view_model.brighten_image()))
        self.button_bright.grid(row=5, column=0, padx=20, pady=10)

        self.button_save = customtkinter.CTkButton(master=root, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Salvar", command=lambda: asyncio.run(self.save_image()))
        self.button_save.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # set default values
        self.button_rotate.configure(state="disabled", text="Rotacionar")
        self.button_translation.configure(state="disabled", text="Translação")
        self.button_scale.configure(state="disabled", text="Escala")
        self.button_bright.configure(state="disabled", text="Brilho")

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

    def create_labels_to_display_images(self):
        self.image_original_label = customtkinter.CTkLabel(root, text="")
        self.image_original_label.grid(row=0, column=1, padx=(20, 0), pady=(20, 0))

        self.image_modify_label = customtkinter.CTkLabel(root, text="")
        self.image_modify_label.grid(row=0, column=2, padx=(20, 0), pady=(20, 0))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    async def open_image(self):
        start = os.path.expanduser('~') + "/Pictures"
        print(start)

        img_path = filedialog.askopenfilename(
            initialdir=start,
            title="Select a image",
            filetypes=(('PNG files', '*.png'), ("jpeg files", "*.jpeg"), ("all files", "*.*"))
        )

        await self.view_model.update_path(img_path)
        await self.view_model.first_load_image_on_labels()

        self.enable_buttons()

    def enable_buttons(self):
        self.button_rotate.configure(state="enable", text="Rotacionar")
        self.button_translation.configure(state="enable", text="Translação")
        self.button_scale.configure(state="enable", text="Escala")
        self.button_bright.configure(state="enable", text="Brilho")

    def update_image_modify_on_label(self, image_update):
        image = customtkinter.CTkImage(image_update, size=(self.weight, self.height))
        self.image_modify_label.configure(image = image)

    def update_image_original_on_label(self, image_update):
        image = customtkinter.CTkImage(image_update, size=(self.weight, self.height))
        self.image_original_label.configure(image=image)

    async def save_image(self):
        location = filedialog.asksaveasfilename(defaultextension=".png")

        await self.view_model.update_location_save_image(location)
        await self.view_model.save_image_on_location()

        print(f"Image saved on: {location}")

    async def open_input_dialog_event(self):
        await self.view_model.update_input_from_dialog(customtkinter.CTkInputDialog(text="Type in a number:", title="Value").get_input())