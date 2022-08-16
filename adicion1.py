#https://www.youtube.com/watch?v=r_6yCPj85cY&list=PLVzwufPir355g7CYmCjuipCodBOC08coo&index=8
from tkinter import *
from tkinter import filedialog
import shutil
import pandas as pd
import cv2#instalarlo pip install opencv-python
#import openpyxl#en condas no necesite instalarlo pip install openpyxl
#from openpyxl import Workbook


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
    dlista_urls={"COVID":"https://sirm.org/category/senza-categoria/covid-19/",
                "Lung_Opacity":"https://www.kaggle.com/c/rsna-pneumonia-detection-challenge/data",
                "Normal":"https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia",
                "Viral Pneumonia":"https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia"}
    opcion1=Label(root,text=value).grid(row=i1)
    opcion2=Label(root,text=value1).grid(row=i1+1)
    imagen1=value1.split('/')
    imagen2=imagen1[len(imagen1)-1]
    #shutil.copy(value1,"/Users/LicHernandoSanabria/MODULOII/PROYECTOFINAL/COVID19/"+value+"/images/"+imagen2) 
    df=pd.read_excel("COVID19/"+value+".metadata.xlsx")
    #print(df)
    ultimo=df.loc[df.index[-1],"FILE NAME"]
    ultimo1=ultimo.split("-")
    ultimo2=ultimo1[-1]
    ultimo_numero=int(ultimo2)
    ultimo_mas1=ultimo_numero+1
    ultimo_file_name=value+"-"+str(ultimo_mas1)
    #print(ultimo_file_name)
    img=cv2.imread(value1,cv2.IMREAD_UNCHANGED)
    ancho=img.shape[0]
    alto=img.shape[1]
    csize=str(ancho)+"*"+str(alto)
    #print(csize)
    extension1=imagen2.split(".")
    extension2=extension1[-1]#extension del archivo de imagen para obtener su tipo
    #print(extension2)
    url1=dlista_urls[value]
    nuevo_nombre=ultimo_file_name+"."+extension2
    print(nuevo_nombre)
    shutil.copy(value1,"/Users/LicHernandoSanabria/MODULOII/PROYECTOFINAL/COVID19/"+value+"/images/"+nuevo_nombre) 
    #print(url1)
    #wb = Workbook()
    #ws = wb.active
    #ws.append([ultimo_file_name, extension2, csize,url1])
    #wb.save("COVID19/"+value+".metadata.xlsx")
    nuevo_registro={"FILE NAME":ultimo_file_name,"FORMAT":extension2,"SIZE":csize,"URL":url1}
    df=df.append(nuevo_registro,ignore_index=True)
    #print(df)
    df.to_excel("COVID19/"+value+".metadata.xlsx",index=False)
    
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