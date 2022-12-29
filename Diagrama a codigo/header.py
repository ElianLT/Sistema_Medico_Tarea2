class empresa:
    def __init__(self,nom="Consultorio Medico",ruc="09999999",tel="09999999",dir="Milagro"):
        self.nombre=nom
        self.ruc=ruc
        self.tel=tel
        
if __name__ == '__main__':
    emp = empresa()
    print("__________________________")
    print("empresa")
    print(emp.nombre)