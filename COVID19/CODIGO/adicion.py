import Covid
import LungOpacity
import Normal
import ViralPneumonia
from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("800x300")
imagenElegida=StringVar()
global imagenElegida1
imagenElegida1=""
directorioR="/Users/LicHernandoSanabria/MODULOII/PROYECTOFINAL/COVID19/"
def select_file():
    filetypes = (
        ('png files', '*.png'),
        ('jpg files', '*.jpg'),
        ('All files', '*.*')
    )
    imagenElegida2 = filedialog.askopenfilename(
        title='Open a file',
        initialdir=directorioR+"/IMAGENESADICION/imagenes",
        filetypes=filetypes)
    imagenElegida.set(imagenElegida2)

def refrescar(value,value1):            
    #print(covid2.nombre)
    imagen1=value1.split('/')
    imagen2=imagen1[len(imagen1)-1]
    if value == "COVID":
        covid2=Covid.Covid('NombreProvisional.png',directorioR)
        covid2.adicionar(imagen2,'95878i.jpg','http://todo2.com','IMAGENESADICION/imagenes','IMAGENESADICION/mascaras')
    if value == "Lung_Opacity":
        LungOpacity1=LungOpacity.LungOpacity('NombreProvisional.png',directorioR)
        LungOpacity1.adicionar(imagen2,'95878i.jpg','http://todo2.com','IMAGENESADICION/imagenes','IMAGENESADICION/mascaras')
    if value == "Normal":
        Normal1=Normal.Normal('NombreProvisional.png',directorioR)
        Normal1.adicionar(imagen2,'95878i.jpg','http://todo2.com','IMAGENESADICION/imagenes','IMAGENESADICION/mascaras')    
    if value == "Viral Pneumonia":
        ViralPneumonia1=ViralPneumonia.ViralPneumonia('NombreProvisional.png',directorioR)
        ViralPneumonia1.adicionar(imagen2,'95878i.jpg','http://todo2.com','IMAGENESADICION/imagenes','IMAGENESADICION/mascaras')    
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

    
btnEnv=Button(root,text="Guardar",command=lambda:refrescar(carpetas.get(),imagenElegida.get())).grid(row=i)
root.mainloop()    


