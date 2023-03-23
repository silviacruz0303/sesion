from tkinter import *

# crear la ventana principal
ventana = Tk()
ventana.geometry("300x300")
ventana.title("Iniciar Sesión")

# crear una etiqueta para el campo de usuario
lbl_usuario = Label(ventana, text="Usuario")
lbl_usuario.pack()

# crear un campo de entrada para el usuario
entrada_usuario = Entry(ventana)
entrada_usuario.pack()

# crear una etiqueta para el campo de contraseña
lbl_contrasena = Label(ventana, text="Contraseña")
lbl_contrasena.pack()

# crear un campo de entrada para la contraseña
entrada_contrasena = Entry(ventana, show="*")
entrada_contrasena.pack()

lbl_confirmacion = Label(ventana, text="Confirmar Contraseña")
lbl_confirmacion.pack()

entrada_confirmacion = Entry(ventana, show="*")
entrada_confirmacion.pack()

# función para manejar el botón de inicio de sesión
def iniciar_sesion():
    if entrada_contrasena.get() == entrada_confirmacion.get():
        print("Sesión iniciada")
        ventana.configure(bg="#00FF00")
    else:
        print("Contraseña incorrecta")


boton_iniciar_sesion = Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
boton_iniciar_sesion.pack(padx=90,pady=3)

lbl_genero = Label(ventana, text="")
lbl_genero.pack()

var_genero = StringVar()
var_genero.set("N/A")


masculino = Radiobutton(ventana, text="Masculino", variable=var_genero, value="M")
masculino.pack()

femenino = Radiobutton(ventana, text="Femenino", variable=var_genero, value="F")
femenino.pack()

# crear una etiqueta para el campo de aceptación de términos y condiciones
terminos = Label(ventana, text="")
terminos.pack()

# crear variable de control para el botón de aceptación de términos y condiciones
var_terminos = BooleanVar()
var_terminos.set(False)

# crear un botón de aceptación de términos y condiciones
chk_terminos = Checkbutton(ventana, text="Acepto los términos y condiciones", variable=var_terminos)
chk_terminos.pack()


ventana.mainloop()