from abc import ABC,abstractmethod 
from personal import paciente, PersonalMedico
import os

class diagnostico():
    def __init__(self,diagnostico, horario):
        self.diagnostico = diagnostico
        self.horario = horario
        
    def mostrardiagnostico(self):
        print(f"Horario: ",self.horario)
        print(f"Diagnostico Medico:",self.diagnostico)
        
if __name__ == '__main__':
    os.system("cls")
    medico = PersonalMedico("Ricardo","099999999","ri@gmail.com","0999999")
    paciente = paciente("Maria","099999999","ma@gmail.com","099999999","Femenino","25")    
    dgnostico = diagnostico("Dolor Estomacal","3:00 PM")
    medico.mostrarusuario()
    paciente.mostrarusuario()
    dgnostico.mostrardiagnostico()
    