class carrito:
    def __init__(self, request):
        self.request=request #En la variable request almacenamos la peticion self.request
        self.session=request.session #Se inicia la sesion en la variable
        carrito=self.session.get("carrito") #Se iguala la sesion del usuario a esa variable carrito 
        if not carrito:
            carrito=self.session["carrito"]={}
        
        self.carrito=carrito

    def agregar(self, producto):
        if(str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,
            }
        else:
            for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break

        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"]=self.carrito #se iguala la variable a la sesion del carrito
        self.session.modified=True
    
    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar_carrito()

    def restar(self, producto):
        for key, value in self.carrito.items():
                if key==str(producto.id):
                    varResta=1
                    value["cantidad"]=value["cantidad"]-varResta
                    value["precio"]=float(value["precio"])-producto.precio
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
               
        self.guardar_carrito() 

    
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True




