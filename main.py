# encoding: utf-8
import os
import re
import linecache
from math import sqrt
import Hillclimber
import SimulatedAnnealing

def mainf():
    os.system("cls")
    print("\t---------- PROBLEMA DO CAIXEIRO VIAJANTE EM GRAFO COMPLETO----------\n")
    print("\n\t1.   Usar grafo de teste (att48.tsp.txt);" + "\n\t2.   Inserir grafo;" +
         "\n\t3.   Sair.")

    op = int(input("\nDigite sua opcao: "))

    if(op == 1):
        preenche("att48.tsp.txt")
    elif(op == 2):
        nome = input("\nInforme o nome do arquivo entre aspas (.txt): ")
        preenche(nome)
    else:
        os.system("cls")
        exit()


def preenche(nome):
    fileName = nome
    file = open(fileName, mode="r").readlines()
    for line1 in file:
        custoParcial = []
        str1 = re.sub(' +', ' ',line1)
        str1 = str1.split(" ")
        formataCoordenadas.append([str1[1],str1[2]]) 
        custos.append(custoParcial)
        for line2 in file:
            str2 = re.sub(' +', ' ',line2)
            str2 = str2.split(" ")
            valorCusto = sqrt(((float(str1[1])-float(str2[1]))**2)+((float(str1[2])-float(str2[2]))**2))
            custoParcial.append(float(valorCusto))

    mainMenu()

def mainMenu():
    os.system("cls")

    op = 0
    while True:
        if op != 3:
            print("\t---------- PROBLEMA DO CAIXEIRO VIAJANTE ----------\n")
            print("\n\t1.   Algoritmo do Hill Climber;" + "\n\t2.   Simulated Annealing;" +
                 "\n\t3.   Sair.")
            op = int(input("\nDigite sua opcao: "))
        if op == 3:
            mainf()
        if op == 2:
            coordXu = 0.0
            coordXv = 0.0
            coordYu = 0.0
            coordYv = 0.0
            coord1 = 0.0
            coord2 = 0.0
            coord3 = 0.0
            coord4 = 0.0
            current = 0.0
            result =  float("inf")
            os.system("cls")
            print("Caso A: \n")
            for i in range(10):
                x1 = int(formataCoordenadas[i][0])
                x2 = int(formataCoordenadas[i][1])
                for y in range(10):
                    x3 = int(formataCoordenadas[i][0])
                    x4 = int(formataCoordenadas[i][1])
                    Sa1 = SimulatedAnnealing.SimulatedAnnealing(x1 ,x2, x3, x4 ,10 ,5 ,0.95 ,20)
                    coord1, coord2, coord3, coord4, current = Sa1.Start()
                    if current < result:
                        coordXu = coord1
                        coordYu = coord2
                        coordXv = coord3
                        coordYv = coord4
                        result = current
            print("Xu= ",coordXu)
            print("Yu = ",coordYu)
            print("Xv = ",coordXv)
            print("Yv = ",coordYv)
            print("resultados = ",result)
            print("Esta e a soluçao do caso A. \nPrecione qualquer tecla para ir ao caso B. \n")
            os.system("pause")
            print("Caso B: \n")
            for i in range(10):
                y1 = int(formataCoordenadas[i][0])
                y2 = int(formataCoordenadas[i][1])
                for y in range(10):
                    y3 = int(formataCoordenadas[i][0])
                    y4 = int(formataCoordenadas[i][1])
                    Sa2 = SimulatedAnnealing.SimulatedAnnealing(y1 ,y2, y3, y4,100 ,10 ,0.9 ,25)
                    coord1, coord2, coord3, coord4, current = Sa2.Start()
                    if current < result:
                        coordXu = coord1
                        coordYu = coord2
                        coordXv = coord3
                        coordYv = coord4
                        result = current
            print("Xu= ",coordXu)
            print("Yu = ",coordYu)
            print("Xv = ",coordXv)
            print("Yv = ",coordYv)
            print("resultados = ",result)

            os.system("pause")
            os.system("cls") 
            
        if op == 1:
            os.system("cls")

            s1,s2 = Hillclimber.hillClimbing(custos)
            print("the current solution is: %s\nthe current route lenght is: %s\n"%(s1, s2))

            os.system("pause")
            os.system("cls")
            
formataCoordenadas = []
custos = []
mainf()

