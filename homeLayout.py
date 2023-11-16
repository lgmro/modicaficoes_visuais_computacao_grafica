import customtkinter
import os
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import simpledialog

class HomeLayout:
    def __init__(self, rotateImageUseCase, translationImageUseCase, scaleImageUseCase):
        # Variables
        global root
        self.rotateImageUseCase = rotateImageUseCase
        self.translationImageUseCase = translationImageUseCase
        self.scaleImageUseCase = scaleImageUseCase
        self.img_path = ""

        # Creating root
        root = customtkinter.CTk()
        root.geometry(f"{1300}x{580}")
        root.title("Modificações Visuais em Imagem")

        # configure grid layout (4x4)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure((2, 3), weight=0)
        root.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(root, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Opções", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Buttons
        self.button_open_image = customtkinter.CTkButton(self.sidebar_frame, command=self.openImage, text="Abrir Imagem")
        self.button_open_image.grid(row=1, column=0, padx=20, pady=10)

        self.button_rotate = customtkinter.CTkButton(self.sidebar_frame, text="Rotacionar", command=self.rotateImage)
        self.button_rotate.grid(row=2, column=0, padx=20, pady=10)

        self.button_translation = customtkinter.CTkButton(self.sidebar_frame, text="Translação", command=self.translationImage)
        self.button_translation.grid(row=3, column=0, padx=20, pady=10)

        self.button_save = customtkinter.CTkButton(master=root, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Salvar", command=self.save)
        self.button_save.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # set default values  
        self.button_rotate.configure(state="disabled", text="Rotacionar")
        self.button_translation.configure(state="disabled", text="Translação") 

        # Settings of app
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Aparência:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Escala do aplicativo:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry 
        self.entry = customtkinter.CTkEntry(root, placeholder_text="Salvar")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        root.mainloop()

    def openImage(self):
        self.img_path = filedialog.askopenfilename(
            initialdir="/picture", 
            title="Select a image",
            filetypes=(('PNG files', '*.png'), ("jpeg files", "*.jpeg"), ("all files", "*.*"))
        )

        im = Image.open(self.img_path)

        print(im.size)
        print(type(im.size))

        weight, height = im.size
        print('width: ', weight)
        print('height:', height)

        if weight > 600:
            weight = 600
        if height > 500:
            height = 500

        self.image = customtkinter.CTkImage(Image.open(os.path.join(self.img_path)), size=(weight, height))
        self.image_label = customtkinter.CTkLabel(root, text="", image=self.image)
        self.image_label.grid(row=0, column=1, padx=(20, 0), pady=(20, 0))

        self.image_modify = customtkinter.CTkImage(Image.open(os.path.join(self.img_path)), size=(weight, height))
        self.image_modify_label = customtkinter.CTkLabel(root, text="", image=self.image_modify)
        self.image_modify_label.grid(row=0, column=2, padx=(20, 0), pady=(20, 0))

        self.button_rotate.configure(state="enable", text="Rotacionar")
        self.button_translation.configure(state="enable", text="Translação")

    def save(self):
        pass

    def open_input_dialog_event(self):
        return customtkinter.CTkInputDialog(text="Type in a number:", title="Value").get_input()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    def rotateImage(self):
        global value
        value = self.open_input_dialog_event()
        image = self.rotateImageUseCase.execute(self.image_modify, value)
        self.image_modify_label.configure(image = image)

    def translationImage(self):
        global value
        value = self.open_input_dialog_event()
        image = self.translationImageUseCase.execute(self.image_modify, value)
        self.image_modify_label.configure(image = image)

    def scaleImage(self):
        global value
        value = self.open_input_dialog_event()
        image = self.scaleImageUseCase.execute(self.image_modify, value)
        self.image_modify_label.configure(image = image)

