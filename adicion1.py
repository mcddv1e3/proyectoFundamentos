#https://www.youtube.com/watch?v=r_6yCPj85cY&list=PLVzwufPir355g7CYmCjuipCodBOC08coo&index=8
from tkinter import *
from tkinter import filedialog
import shutil
root=Tk()
root.geometry("800x300")
imagenElegida=StringVar()
global imagenElegida1
imagenElegida1=""
def select_file():
    filetypes = (
        ('png files', '*.png'),
        ('jpg files', '*.jpg'),
        ('All files', '*.*')
    )

    imagenElegida2 = filedialog.askopenfilename(
        title='Open a file',
        initialdir='/Users/LicHernandoSanabria/MODULOII/PROYECTOFINAL/COVID19/imagenes',
        filetypes=filetypes)
    imagenElegida.set(imagenElegida2)

def refrescar(value,value1,i1):
    opcion1=Label(root,text=value).grid(row=i1)
    opcion2=Label(root,text=value1).grid(row=i1+1)
    imagen1=value1.split('/')
    imagen2=imagen1[len(imagen1)-1]
    shutil.copy(value1,"/Users/LicHernandoSanabria/MODULOII/PROYECTOFINAL/COVID19/"+value+"/images/"+imagen2) 
i=0

btnEnv=Button(root,text="Leer Archivo",command=select_file).grid(row=i)    
i=i+1
titulo=Label(root,text="Elija donde guardar").grid(row=i)
elegir=["COVID","Lung_Opacity","Normal","Viral Pneumonia"]
carpetas=StringVar()
carpetas.set("COVID")
i=i+1
for elige in elegir:    
    Radiobutton(root,text=elige,value=elige,variable=carpetas).grid(row=i)
    i=i+1
    
btnEnv=Button(root,text="Guardar",command=lambda:refrescar(carpetas.get(),imagenElegida.get(),i+1)).grid(row=i)
root.mainloop()