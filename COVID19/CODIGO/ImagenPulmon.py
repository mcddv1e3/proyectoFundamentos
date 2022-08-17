import pandas as pd
import cv2#instalarlo pip install opencv-python
import shutil
class ImagenPulmon:
  def __init__(self,nombre,raiz,directorio):
    self.nombre=nombre#el nombre de la imagen
    self.raiz=raiz#el directorio raiz donde se trabajara por ejemplo c:/PROYECTOFINAL
    self.directorio=directorio#el directorio donde pertenece la imagen ejm. COVID, Lung_Opacity    
  def adicionar(self,nombre_imagen,nombre_mascara,url,dir_imagenes,dir_mascaras):
    #print('nombre '+self.nombre+' directorio '+str(self.directorio)+' nombre imagen a adicionar '+nombre_imagen)
    """
    -se obtiene la extension del archivo de imagen para obtener su tipo
    -determinamos el nombre que nos corresponde para grabar:obtenemos el ultimo nombre (FILE NAME )
    registro del excel donde vamos a grabar para poder determinar el nombre que me toca
    que es sumar en 1 el ultimo nombre, usamos un data frame para esto (df)
    -obteniendo los datos de la imágen:se obtiene el ancho, alto de la imagen a ser copiada
    -se agrega al excel el registro correspondiente
    """
    #obteniendo la extension del archivo de imagen para obtener su tipo
    extension1=nombre_imagen.split(".")
    extension2=extension1[-1]
    #print(extension2)
    #determinamos el nombre que nos corresponde para grabar
    df=pd.read_excel(self.raiz+"/"+self.directorio+".metadata.xlsx")
    #print(df)
    ultimo=df.loc[df.index[-1],"FILE NAME"]
    ultimo1=ultimo.split("-")
    ultimo2=ultimo1[-1]
    ultimo_numero=int(ultimo2)
    ultimo_mas1=ultimo_numero+1
    ultimo_file_name_nextension=self.directorio+"-"+str(ultimo_mas1)
    ultimo_file_name=self.directorio+"-"+str(ultimo_mas1)+"."+extension2
    print(ultimo_file_name)
    #obteniendo los datos de la imágen ancho alto
    imagen_copiar=self.raiz+"/"+dir_imagenes+"/"+nombre_imagen
    img=cv2.imread(imagen_copiar,cv2.IMREAD_UNCHANGED)
    ancho=img.shape[0]
    alto=img.shape[1]
    csize=str(ancho)+"*"+str(alto)
    #print(csize)
    shutil.copy(imagen_copiar,self.raiz+"/"+self.directorio+"/images/"+ultimo_file_name)
    #agregando al excel el registro correspondiente
    nuevo_registro={"FILE NAME":ultimo_file_name_nextension,"FORMAT":extension2,"SIZE":csize,"URL":url}
    df=df.append(nuevo_registro,ignore_index=True)
    df.to_excel(self.raiz+"/"+self.directorio+".metadata.xlsx",index=False)