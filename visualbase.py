import tkinter as tk
from tkinter import messagebox
from modelobd import OperacionDB

class App:
    """
    Esta clase establece la visual de la ventana para modificar datos y la conexion con la base de datos.
    """
    def __init__(self, root):
        """
        Establece valores de variables y la visual de la ventana de modificacion.
        """
        root.title("Integrado!")
        width=335
        height=560
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        labelValida=tk.Label(root)
        labelValida["fg"] = "#333333"
        labelValida["justify"] = "center"
        labelValida["text"] = "label"
        labelValida.place(x=160,y=460,width=171,height=30)

        self.botonconsulta=tk.Button(root)
        self.botonconsulta["bg"] = "#fafafa"
        self.botonconsulta["fg"] = "#3d3d3d"
        self.botonconsulta["justify"] = "center"
        self.botonconsulta["text"] = "Consultar"
        self.botonconsulta.place(x=230,y=160,width=70,height=25)
        self.botonconsulta["command"] = self.bconsulta

        self.botonelimina=tk.Button(root)
        self.botonelimina["bg"] = "#fafafa"
        self.botonelimina["fg"] = "#3d3d3d"
        self.botonelimina["justify"] = "center"
        self.botonelimina["text"] = "Eliminar"
        self.botonelimina.place(x=230,y=130,width=70,height=25)
        self.botonelimina["command"] = self.belimina

        labelValida=tk.Label(root)
        labelValida["fg"] = "#333333"
        labelValida["justify"] = "center"
        labelValida["text"] = "Usuario:"
        labelValida.place(x=10,y=30,width=171,height=30)

        self.validaEntry=tk.Entry(root)
        self.validaEntry["borderwidth"] = "1px"
        self.validaEntry["fg"] = "#333333"
        self.validaEntry["justify"] = "left"
        self.validaEntry["text"] = "Valida_entry"
        self.validaEntry["relief"] = "sunken"
        self.validaEntry.place(x=160,y=30,width=141,height=30)

        labeldata=tk.Label(root)
        labeldata["fg"] = "#333333"
        labeldata["justify"] = "center"
        labeldata["text"] = "Ingreso Data:"
        labeldata.place(x=10,y=60,width=171,height=30)

        self.dataEntry=tk.Entry(root)
        self.dataEntry["borderwidth"] = "1px"
        self.dataEntry["fg"] = "#333333"
        self.dataEntry["justify"] = "left"
        self.dataEntry["text"] = "data_entry"
        self.dataEntry["relief"] = "sunken"
        self.dataEntry.place(x=160,y=60,width=141,height=30)

        self.cbPassword=tk.Checkbutton(root)
        self.cbPassword["fg"] = "#333333"
        self.cbPassword["text"] = "Password"
        self.cbPassword.place(x=40,y=140,width=90,height=25)
        self.cbPassword["offvalue"] = "0"
        self.cbPassword["onvalue"] = "1"
        self.cbPassword["command"] = self.bcbpassword

        self.cbNombre=tk.Checkbutton(root)
        self.cbNombre["fg"] = "#333333"
        self.cbNombre["text"] = "Nombre"
        self.cbNombre.place(x=40,y=170,width=90,height=25)
        self.cbNombre["offvalue"] = "0"
        self.cbNombre["onvalue"] = "1"
        self.cbNombre["command"] = self.bcbnombre

        self.cbApellido=tk.Checkbutton(root)
        self.cbApellido["fg"] = "#333333"
        self.cbApellido["text"] = "Apellido"
        self.cbApellido.place(x=40,y=200,width=90,height=25)
        self.cbApellido["offvalue"] = "0"
        self.cbApellido["onvalue"] = "1"
        self.cbApellido["command"] = self.bcbapellido

        self.cbTelefono=tk.Checkbutton(root)
        self.cbTelefono["fg"] = "#333333"
        self.cbTelefono["text"] = "Telefono"
        self.cbTelefono.place(x=130,y=140,width=90,height=25)
        self.cbTelefono["offvalue"] = "0"
        self.cbTelefono["onvalue"] = "1"
        self.cbTelefono["command"] = self.bcbtelefono

        self.cbDNI=tk.Checkbutton(root)
        self.cbDNI["fg"] = "#333333"
        self.cbDNI["text"] = "DNI"
        self.cbDNI.place(x=130,y=170,width=90,height=25)
        self.cbDNI["offvalue"] = "0"
        self.cbDNI["onvalue"] = "1"
        self.cbDNI["command"] = self.bcbdni

    def bconsulta(self):
        """
        Metodo para llamar la clase OperacionDB / metodo: Consulta y le ingresa el dato de usuario.
        """
        #print(self.usuario)
        try:
            consulta = OperacionDB().consultageneral(self.validaEntry.get())
            messagebox.showinfo(message=consulta, title="Consulta")
        except:
            messagebox.showinfo(message="Usuario no encontrado!", title="Error.")
            
    def belimina(self):
        """
        Metodo para eliminar usuarios a traves del ingreso del usuario y el password.
        """
        try:
            OperacionDB().borrar(self.validaEntry.get(), self.dataEntry.get())
            messagebox.showinfo(message="Usuario borrado correctamente.", title="Borrado exitoso.")
        except:
            messagebox.showinfo(message="Error!.", title="Error!")

    def bcbpassword(self):
        """
        Metodo para modificar las password de un usuario en la base de datos.
        """
        try:
            OperacionDB().modificarusuario("Password",self.dataEntry.get(), self.validaEntry.get())
            messagebox.showinfo(message=f"Password de {self.validaEntry.get()} modificado.", title="Modificación")
        except:
            messagebox.showinfo(message="Error en el cambio de password.", title="Error.")

    def bcbnombre(self):
        """
        Metodo para modificar el nombre de un usuario en la base de datos.
        """
        try:
            OperacionDB().modificarusuario("Nombre",self.dataEntry.get(), self.validaEntry.get())
            messagebox.showinfo(message=f"Nombre de {self.validaEntry.get()} modificado.", title="Modificación")
        except:
            messagebox.showinfo(message="Error en el cambio de nombre.", title="Error.")

    def bcbapellido(self):
        """
        Metodo para modificar el apellido de un usuario en la base de datos.
        """
        try:
            OperacionDB().modificarusuario("Apellido",self.dataEntry.get(), self.validaEntry.get())
            messagebox.showinfo(message=f"Apellido de {self.validaEntry.get()} modificado.", title="Modificación")
        except:
            messagebox.showinfo(message="Error en el cambio de password.", title="Error.")

    def bcbtelefono(self):
        """
        Metodo para modificar el telefono de un usuario en la base de datos.
        """
        try:
        
            OperacionDB().modificarusuario("Telefono",int(self.dataEntry.get()), self.validaEntry.get())
            messagebox.showinfo(message=f"Telefono de {self.validaEntry.get()} modificado.", title="Modificación")
        except:
            messagebox.showinfo(message="Error en el cambio de telefono.", title="Error.")

    def bcbdni(self):
        """
        Metodo para modificar el dni de un usuario en la base de datos.
        """
        try:
            OperacionDB().modificarusuario("Dni",int(self.dataEntry.get()), self.validaEntry.get())
            messagebox.showinfo(message=f"DNI de {self.validaEntry.get()} modificado.", title="Modificación")
        except:
            messagebox.showinfo(message="Error en el cambio de DNI.", title="Error.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
