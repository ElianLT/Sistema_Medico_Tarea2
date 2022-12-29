from abc import ABC,abstractmethod 
import os

class personal(ABC):
    id = 0
    def __init__(self, nom, ced, correo, tel):
        self.id = personal.id
        personal.id += 1
        self.nombre = nom
        self.cedula = ced
        self.correo = correo
        self.telefono = tel
        
    @property
    def codigo(self):
        return self.id
    
    @abstractmethod
    def mostrarusuario(self):
        pass
    
class PersonalMedico(personal):
    def __init__(self, nom, ced, correo, tel):
        super().__init__(nom, ced, correo, tel)
        
        
    def mostrarusuario(self):
        print(f"Medico:",self.nombre, "Cedula:",self.cedula, "Telefono:",self.telefono, "Correo:",self.correo)
        

class paciente(personal):
    def __init__(self, nom, ced, correo, tel, genero, edad):
        super().__init__(nom, ced, correo, tel)
        self.genero = genero
        self.edad = edad
        
    def mostrarusuario(self):
        print(f"Paciente:",self.nombre, "Cedula:",self.cedula)
        
if __name__ == '__main__':
    os.system("cls")  
    print("________Paciente_________")       
    personal = PersonalMedico("Ricardo","09999999","ri@gmail.com","099999999")
    paciente1 = paciente("Maria","09999999","ma@gmail.com","099999999","Femenino","25")
    personal.mostrarusuario()
    paciente1.mostrarusuario()