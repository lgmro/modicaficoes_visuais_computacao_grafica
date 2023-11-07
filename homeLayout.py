import tkinter
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import simpledialog

class HomeLayout:
    def __init__(self, rotateImageUseCase, translationImageUseCase, scaleImageUseCase):
        # Variables
        global imageView
        global root
        self.rotateImageUseCase = rotateImageUseCase
        self.translationImageUseCase = translationImageUseCase
        self.scaleImageUseCase = scaleImageUseCase

        # Creating root
        root = tkinter.Tk()
        root.geometry("500x350")
        root.title("Modificações Visuais em Imagem")

        # Creating menu
        menu = tkinter.Frame(root, bg='#c3c3c3')
        menu.pack(side=tkinter.LEFT, fill=tkinter.Y)
        menu.configure(width=100)

        # Creating image viewer
        imageView = tkinter.Frame(root, bg="#FFFFFF", highlightbackground='black', highlightthickness=2)
        imageView.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)


        button = tkinter.Button(master=menu, text="Abrir Imagem", command=self.openImage)
        button.pack(side=tkinter.TOP,fill=tkinter.X, pady=5)

        button = tkinter.Button(master=menu, text="Rotacionar", command=self.rotateImage)
        button.pack(side=tkinter.TOP,fill=tkinter.X, pady=5)

        button = tkinter.Button(master=menu, text="Translação", command=self.translationImage)
        button.pack(side=tkinter.TOP,fill=tkinter.X, pady=5)

        button = tkinter.Button(master=menu, text="Escalar", command=self.scaleImage)
        button.pack(side=tkinter.TOP,fill=tkinter.X, pady=5)

        root.mainloop()

    def openImage(self):
        global image
        root.filename = filedialog.askopenfilename(initialdir="/picture", 
                                            title="Slect a image",
                                            filetypes=(("jpeg files", "*.jpeg"),("all files", "*.*"))
                                           )

        tkinter.Label(imageView, text=root.filename, bg="#FFFFFF").pack(side=tkinter.TOP)
        image = ImageTk.PhotoImage(Image.open(root.filename))
        imageLabel = tkinter.Label(imageView, image=image, bg="#FFFFFF")
        imageLabel.pack(fill=tkinter.BOTH, expand=True)
    
    def enterValueFloat(self):
        return simpledialog.askfloat("Grau", "Entre com o grau", parent=root)
    
    def rotateImage(self):
        global value
        value = self.enterValueFloat()
        self.rotateImageUseCase.execute()

    def translationImage(self):
        global value
        value = self.enterValueFloat()
        self.translationImageUseCase.execute()

    def scaleImage(self):
        global value
        value = self.enterValueFloat()
        self.scaleImageUseCase.execute()

