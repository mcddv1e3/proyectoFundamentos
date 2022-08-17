import ImagenPulmon
class LungOpacity(ImagenPulmon.ImagenPulmon):
    def __init__(self,nombre,raiz):
        super().__init__(nombre,raiz,"Lung_Opacity")