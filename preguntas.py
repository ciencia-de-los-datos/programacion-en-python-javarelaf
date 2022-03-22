#importar librerias permitidas
import csv
from collections import Counter 
from operator import itemgetter
import datetime
from functools import reduce


#importar datos
f=open('data.csv',"r")
reader=csv.reader(f,delimiter="\t")
datos=list()
for fila in reader:
    datos.append(fila)

#Pregunta 1
def pregunta_01():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter="\t")
 datos=list()
 for fila in reader:
    datos.append(fila)
 # 
 suma=0
 for fila in datos:
    suma=suma+int(fila[1])
 suma
 return suma


#Pregunta_02
def pregunta_02():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter="\t")
 datos=list()
 for fila in reader:
    datos.append(fila)
 #
 datos.sort(key=itemgetter(0),reverse=False)
 letras=list()
 for fila in datos:
  letras.append(fila[0])
 count=Counter(letras)
 c=list(count.items())
 return c
pass

#pregunta_03 - rapido
def  pregunta_03():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter="\t")
 datos=list()
 for fila in reader:
  datos.append(fila)
 #
 out=list()
 letras=list()
 for fila in datos:
  letras.append(fila[0])
 set_letras=set(letras)
 unique_letras=(list(set_letras))
 unique_letras.sort()
 for letra in unique_letras:
    suma=0
    for fila in datos:
        if letra == fila[0]:
         suma=suma+int(fila[1])
    out.append((letra,suma))
 
 return out
pass


#pregunta_04
def pregunta_04():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter=";")
 datos=list()
 for fila in reader:
      datos.append(fila)
 #
 fechas=list()
 mes=list()
 fecha3=list()
 for fila in datos:
  fechas.append(fila[2])
 for fecha in fechas:
  fecha2=fecha.replace('/','-')
  fecha3.append(fecha2.split("-"))
 
 for fecha in fecha3:
  mes.append(fecha[1])
 
 mes.sort(reverse=False)
 
 
 return list(Counter(mes).items())

pass

#Pregunta 5
def pregunta_05():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter=";")
 datos=list()
 for fila in reader:
      datos.append(fila)
 #
 out=list()
 letras=list()
 
 for fila in datos:
  letras.append(fila[0])
 set_letras=set(letras)
 unique_letras=(list(set_letras))
 unique_letras.sort()
 for letra in unique_letras:
    numeros=[]
    for fila in datos:
        if letra == fila[0]:
         numeros.append(int(fila[1]))
                 
    out.append((letra,max(numeros),min(numeros)))
 
 return out

pass


#pregunta_06
def pregunta_06():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter=";")
 datos=list()
 for fila in reader:
      datos.append(fila)
 #
 out=[]
 out_aux=[]
 clave=[]
 letras_aux=[]

 for fila in datos:
     claves=fila[4].split(',')
     clave=claves+clave

 for objeto in clave:
     pair=objeto.split(':')
     out_aux.append((pair[0],int(pair[1])))
 
 for pair in out_aux:
     letras_aux.append(pair[0])
  
 letras=(list(set(letras_aux)))
 letras.sort()

 for letra in letras: 
     numeros=[]
     for pair in out_aux:
         if letra == pair[0]:
             numeros.append(int(pair[1]))
     out.append((letra,min(numeros),max(numeros)))

 return out

pass

#Pregunta_07
def pregunta_07():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter=";")
 datos=list()
 for fila in reader:
      datos.append(fila)
 #
 numeros=[]
 out=[]
 for fila in datos:
     numeros.append(fila[1])
 set_numeros=set(numeros)
 unique_numeros=(list(set_numeros))
 unique_numeros.sort()
 for numero in unique_numeros:
  letras=[]
  for fila in datos:
      if numero == fila[1]:
         letras.append(fila[0])
         
  out.append((numero,letras))
  

 return out
pass

#Pregunta_08
def pregunta_08():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter=";")
 datos=list()
 for fila in reader:
      datos.append(fila)
 #
 numeros=[]
 out=[]
 x=0
 for fila in datos:
     numeros.append(fila[1])
 set_numeros=set(numeros)
 unique_numeros=(list(set_numeros))
 unique_numeros.sort()
 for numero in unique_numeros:
  letras=[]
  for fila in datos:
        if (numero == fila[1]) & (fila[0] not in letras):
         letras.append(fila[0])
         letras.sort()
  out.append((numero,letras))
  

 return out
pass

#pregunta_09
def pregunta_09():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter=";")
 datos=list()
 for fila in reader:
      datos.append(fila)
 #
 out=[]
 out_aux=[]
 clave=[]
 

 for fila in datos:
     claves=fila[4].split(',')
     clave=claves+clave

 for objeto in clave:
     pair=objeto.split(':')
     out_aux.append(pair[0])

 out_aux_set=(list(set(out_aux)))
 out_aux_set.sort()

 for letras in out_aux_set:
     count=0
     for letra in out_aux:
         if letras == letra:
             count=count+1
     out.append((letras,count))
 
 return out
pass

#pregunta_10
def pregunta_10():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter=";")
 datos=list()
 for fila in reader:
      datos.append(fila)
 #
 out=[]
 iniciales=[]
 letras=[]
 claves=[]
 
 for fila in datos: 
     iniciales.append(fila[0])
     letras.append(fila[3].split(','))
     claves.append(fila[4].split(','))
    
 count=0
 for fila in iniciales: 
     out.append((fila,len(letras[count]),len(claves[count])))
     count=count+1

 return out
pass

#pregunta_11
def pregunta_11():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter=";")
 datos=list()
 for fila in reader:
      datos.append(fila)
 #
 out={}
 letras_grupo=[]
 letras_ind=[]
 numeros=[]
 for fila in datos: 
     letras_grupo.append(fila[3].split(','))
     numeros.append(int(fila[1]))

 
 for letra in letras_grupo: 
     for l in letra:
      letras_ind.append(l)
 letras_set=(list(set(letras_ind)))
 letras_set.sort()

 for l in letras_set:
     suma=0
     cuenta=0
     for fila in letras_grupo:
         if l in fila:
           suma= suma+numeros[cuenta]
         cuenta=cuenta+1
     out[l]=suma

 return out

pass

#pregunta_12
def pregunta_12():
 f=open('data.csv',"r")
 reader=csv.reader(f,delimiter=";")
 datos=list()
 for fila in reader:
      datos.append(fila)
 #
 out={}
 letras=[]
 clave=[]
 for fila in datos:
     letras.append(fila[0])
     
 
 numeros=[]
 set_letras=(list(set(letras)))
 set_letras.sort()
 
 for letra in letras:
  suma=0
  for fila in datos: 
     if letra == fila[0]:
            
      for lista in fila[4].split(','): 
         valor=lista.split(':')
         suma=suma+int(valor[1])           

     
  out[letra]=suma


 return dict(sorted(out.items()))

pass