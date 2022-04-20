from alumnos import Alumno
from plantas import Planta 
from hierba import Hierba
from rabano import Rabano
from violeta import Violeta
from trebol import Trebol
from vasos import Vasos
import random as rd 

def vasos(estudiantes, plantas, vasos1, vasos2):
    #tengo que dividir esto en dos filas 
    for i in range(len(estudiantes)):
        for x in plantas:
            if i <= (len(estudiantes)/2): 
                vasos1.append(x)
            else: 
                vasos2.append(x)

def repartir_plantas(vasos,trebol,hierba,rabano,violeta,estudiantes):
    
    for j in range(len(estudiantes)):
        remover = []
        alumno = Alumno(estudiantes[j])
        print("al estudiante: ",alumno.estudiante,"\t")
        print("le corresponden las siguientes plantitas: ")
        for x in range(2):
            planta_asignada = Vasos(rd.choice(vasos))
            if planta_asignada == trebol.nombre:
                print(trebol.nombre, end = " ")
            elif planta_asignada == violeta.nombre:
                print(violeta.nombre, end = " ")
            elif planta_asignada == hierba.nombre:
                print(hierba.nombre, end = " ")
            else:
                print(rabano.nombre, end = " ")
            print(vasos)
            remover.append(planta_asignada)
            vasos.remove(remover[x])
            print(vasos)
        print("\t")
        print("\t")

def main():
    estudiantes =  ["Alicia", "Marit", "Pepito", "David", "Eva", "Lucia", "Rocio", "Andres", "Jose", "Belen", "Sergio", "larry"]
    plantas = ["hierba", "violeta", "trebol", "rabano"]
    vasos_fila1 = []
    vasos_fila2 = []
    alumno = []
    trebol = Trebol()
    violeta = Violeta()
    hierba = Hierba()
    rabano = Rabano()
    vasos(estudiantes, plantas, vasos_fila1, vasos_fila2)
    print("primera fila: ")
    repartir_plantas(vasos_fila1,trebol,hierba,rabano,violeta,estudiantes)
    print("segunda fila: ")
    repartir_plantas(vasos_fila2,trebol,hierba,rabano,violeta,estudiantes)

if __name__ == "__main__":
    main()
