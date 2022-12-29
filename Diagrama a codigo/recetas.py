from datetime import date
from header import empresa
from personal import paciente
from cita import diagnostico
import os

class Articulo:
    _secuencia=0
    def __init__(self,des,pre,sto):
        Articulo._secuencia += 1
        self.__codigo = Articulo._secuencia
        self.descripcion = des
        self.precio = pre   
        self.stock = sto
    
    @property
    def codigo(self):
        return self.__codigo
        
    def mostrarArticulo(self):
        print(self.codigo,self.descripcion)

class detallereceta:
    _linea=0
    def __init__(self,articulo,cantidad):
        detallereceta._linea += 1
        self.linea = detallereceta._linea
        self.articulo = articulo
        self.precio = articulo.precio
        self.cantidad = cantidad


class receta:
    _factura = 0
    iva = 0.12
    def __init__(self,personal,cita):
        receta._factura = receta._factura + 1
        self.factura = "F"+str(receta._factura)
        self.fecha = date.today()
        self.paciente = personal
        self.diagnostico = cita
        self.subtotal = 0
        self.iva = 0
        self.total = 0
        self.detalleventa = []
        
        
    def agregarDetalle(self,articulo,cantidad):
        detalle = detallereceta(articulo,cantidad)
        self.subtotal += round(detalle.precio*detalle.cantidad,2)
        self.iva = round(self.subtotal*receta.iva,2)
        self.total = round(self.subtotal+self.iva,2)
        self.detalleventa.append(detalle)    
    
    def mostrarreceta(self,empNombre,empRuc):
        print("Empresa: {:12} Ruc:{}".format(empNombre,empRuc)) 
        print("Factura#:{:13}Fecha:  {}".format(self.factura,self.fecha))
        self.paciente.mostrarusuario()
        self.diagnostico.mostrardiagnostico()
        print("="*50)
        print("Linea Articulo     Precio Cantidad Subtotal")
        for det in self.detalleventa:
            print("{:5} {:15} {} {:6} {:7}".format(det.linea,det.articulo.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))  
        print("="*23,"Subtotal=> ",self.subtotal)
        print("="*26,"Iva=> ",self.iva)
        print("="*23,"Total=> ",self.total) 
        
os.system("cls")       
empresa = empresa()    
pac = paciente("Maria","09999999","maria@gmai.com","09999999","Femenino","25")
med = diagnostico("Malestar Estomacal","10AM")      
art1 = Articulo("Paracetamol",3,200)
art2 = Articulo("Aspirina",4,100)
rec = receta(pac,med)
rec.agregarDetalle(art1,3)
rec.agregarDetalle(art2,10)
rec.mostrarreceta(empresa.nombre, empresa.ruc)