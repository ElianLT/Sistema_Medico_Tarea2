import os

class historiaclinica:
    id = 0
    def __init__(self, nom,apepa,apema,ced,fnacimiento,edad,antecedentes,correo,telefono):
        self.id = historiaclinica.id
        historiaclinica.id += 1
        self.nom = nom
        self.apellidopaterno = apepa
        self.apellidomaterno = apema
        self.cedula = ced
        self.fechanacimiento = fnacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.correo = correo
        self.telefono = telefono
        
        
        
    @property
    def codigo(self):
        return self.id
    
    def mostrarhistoria(self):
        print(f"ID: ",self.id)
        print(f"Nombre: ",self.nom)
        print(f"Apellido Paterno: ",self.apellidopaterno)
        print(f"Apellido Materno: ",self.apellidomaterno)
        print(f"Cedula: ",self.cedula)
        print(f"Fecha Nacimiento: ",self.fechanacimiento)
        print(f"Edad: ",self.edad)
        print(f"Antecedentes: ",self.antecedentes)
        print(f"Correo: ",self.correo)
        print(f"Telefono: ",self.telefono)
        
os.system("cls")
print(f"="*10, "Historia Clinica", "="*10)
paciente = historiaclinica("Maria","Moreno","Astudillo","099999999","14/07/2000","22","Varicela","ma@gmail.com","099999999")
paciente.mostrarhistoria()
print(f"="*10, "Historia Clinica", "="*10)
