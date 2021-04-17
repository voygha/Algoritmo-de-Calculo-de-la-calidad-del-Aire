"""

donde:
Índice = valor del índice para el contaminante deseado (O3, PM10 o PM2.5), calculado con la Ecuación 1.
C = valor redondeado para la concentración del contaminante
k= constante de proporcionalidad estimada de acuerdo a la ecuación 2
BPHi =valor del punto de corte que es mayor o igual a la concentración a evaluar.
BPLo =valor del punto de corte que es menor o igual a la concentración a evaluar.
IHi =valor del índice que corresponde al valor de BPHi
ILo =valor del índice que corresponde al valor de BPLo
"""
import random

indice=0
c=0
k=0
bphi=0
bplo=0
ihi=0
ilo=0
aux=0
resta=0





bphi= round(random.uniform(0.001,0.604),3)
#bphi=0.070
print("El valor de bphi EL QUE IMPORTA es: ",bphi)

if bphi >= 0.000 and bphi  <= 0.070:
    bplo=round(random.uniform(0,bphi - 0.001),3)
    print("El valor de BpLo es: ", bplo)
    ihi=50
    ilo=0
    k= ihi - ilo
    resta= round((bphi - bplo),3)
    print("El valor de la resta es: ",resta)
    k= round((k / resta),2)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+0.001,0.070),3)
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en ozono es: ", indice)



    bphi=0
    bplo=0
    k=0
    resta=0
    c=0
    indice=0
    print("\n")
    print("\n")
    #SIEMPRE HAY QUE DARLE UNNO MAS
    bphi= round(random.uniform(1,40))
    print("El valor de bphi es: ", bphi)
    #bphi=40
    #SIEMPRE HAY QUE DARLE UNNO MAS
    bplo=round(random.uniform(0,bphi - 1))
    print("El valor de bplo es: ", bplo)
    k= ihi - ilo
    resta= round((bphi - bplo))
    print("El valor de la resta es: ",resta)
    k= round((k / resta),3)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+1,40))
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en Partículas Menores a 10 micrómetros (PM10) es: ", indice)
    


    bphi=0
    bplo=0
    k=0
    resta=0
    c=0
    indice=0
    print("\n")
    print("\n")
    bphi= round(random.uniform(0.0,12.0),1)
    print("El valor de bphi es: ", bphi)
    #bphi=12.0
    bplo=round(random.uniform(0.1,bphi - 0.1),1)
    print("El valor de bplo es: ", bplo)
    k= ihi - ilo
    resta= round((bphi - bplo),1)
    print("El valor de la resta es: ",resta)
    k= round((k / resta),3)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+0.1,12.0),1)
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en Partículas Menores a 2.5 micrómetros (PM2.5) es: ", indice)


    print("\n")
    print("\n")
    print("La Calidad del Aire es BUENA")

"""
AQUI COMIENZA EL SEGUNDO
"""




if bphi >= 0.071 and bphi  <= 0.095:
    bplo=round(random.uniform(0.071,bphi - 0.001),3)
    print("El valor de BpLo es: ", bplo)
    ihi=100
    ilo=51
    k= ihi - ilo
    resta= round((bphi - bplo),3)
    print("El valor de la resta es: ",resta)
    k= round((k / resta),2)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+0.001,0.095),3)
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en ozono es: ", indice)



    bphi=0
    bplo=0
    k=0
    resta=0
    c=0
    indice=0
    print("\n")
    print("\n")
    bphi= round(random.uniform(41,75))
    print("El valor de bphi es: ", bphi)
    #bphi=40
    #SIEMPRE HAY QUE DARLE UNNO MAS
    bplo=round(random.uniform(40,bphi - 1))
    print("El valor de bplo es: ", bplo)
    k= ihi - ilo
    resta= round((bphi - bplo))
    print("El valor de la resta es: ",resta)
    k= round((k / resta),3)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+1,75))
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en Partículas Menores a 10 micrómetros (PM10) es: ", indice)
    


    bphi=0
    bplo=0
    k=0
    resta=0
    c=0
    indice=0
    print("\n")
    print("\n")
    bphi= round(random.uniform(12.2,45.0),1)
    print("El valor de bphi es: ", bphi)
    #bphi=12.0
    bplo=round(random.uniform(12.1,bphi - 0.1),1)
    print("El valor de bplo es: ", bplo)
    k= ihi - ilo
    resta= round((bphi - bplo),1)
    print("El valor de la resta es: ",resta)
    k= round((k / resta),3)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+0.1,45.0),1)
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en Partículas Menores a 2.5 micrómetros (PM2.5) es: ", indice)


    print("\n")
    print("\n")
    print("La Calidad del Aire es REGULAR")





"""
AQUI COMIENZA EL TERCERO
"""




if bphi >= 0.096 and bphi  <= 0.154:
    bplo=round(random.uniform(0.096,bphi - 0.001),3)
    print("El valor de BpLo es: ", bplo)
    ihi=150
    ilo=101
    k= ihi - ilo
    resta= round((bphi - bplo),3)
    print("El valor de la resta es: ",resta)
    k= round((k / resta),2)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+0.001,0.154),3)
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en ozono es: ", indice)



    bphi=0
    bplo=0
    k=0
    resta=0
    c=0
    indice=0
    print("\n")
    print("\n")
    #SIEMPRE HAY QUE DARLE UNNO MAS
    bphi= round(random.uniform(77,214))
    print("El valor de bphi es: ", bphi)
    #bphi=40
    bplo=round(random.uniform(76,bphi - 1))
    print("El valor de bplo es: ", bplo)
    k= ihi - ilo
    resta= round((bphi - bplo))
    print("El valor de la resta es: ",resta)
    k= round((k / resta),3)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+1,214))
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en Partículas Menores a 10 micrómetros (PM10) es: ", indice)
    


    bphi=0
    bplo=0
    k=0
    resta=0
    c=0
    indice=0
    print("\n")
    print("\n")
    bphi= round(random.uniform(45.2,97.4),1)
    print("El valor de bphi es: ", bphi)
    #bphi=12.0
    bplo=round(random.uniform(45.1,bphi - 0.1),1)
    print("El valor de bplo es: ", bplo)
    k= ihi - ilo
    resta= round((bphi - bplo),1)
    print("El valor de la resta es: ",resta)
    k= round((k / resta),3)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+0.1,97.4),1)
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en Partículas Menores a 2.5 micrómetros (PM2.5) es: ", indice)


    print("\n")
    print("\n")
    print("La Calidad del Aire es MALA")








"""
AQUI COMIENZA EL CUARTO
"""




if bphi >= 0.155 and bphi  <= 0.204:
    bplo=round(random.uniform(0.155,bphi - 0.001),3)
    print("El valor de BpLo es: ", bplo)
    ihi=200
    ilo=151
    k= ihi - ilo
    resta= round((bphi - bplo),3)
    print("El valor de la resta es: ",resta)
    k= round((k / resta),2)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+0.001,0.204),3)
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en ozono es: ", indice)



    bphi=0
    bplo=0
    k=0
    resta=0
    c=0
    indice=0
    print("\n")
    print("\n")
    #SIEMPRE HAY QUE DARLE UNNO MAS
    bphi= round(random.uniform(216,354))
    print("El valor de bphi es: ", bphi)
    #bphi=40
    bplo=round(random.uniform(215,bphi - 1))
    print("El valor de bplo es: ", bplo)
    k= ihi - ilo
    resta= round((bphi - bplo))
    print("El valor de la resta es: ",resta)
    k= round((k / resta),3)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+1,354))
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en Partículas Menores a 10 micrómetros (PM10) es: ", indice)
    


    bphi=0
    bplo=0
    k=0
    resta=0
    c=0
    indice=0
    print("\n")
    print("\n")
    bphi= round(random.uniform(97.6,150.4),1)
    print("El valor de bphi es: ", bphi)
    #bphi=12.0
    bplo=round(random.uniform(97.5,bphi - 0.1),1)
    print("El valor de bplo es: ", bplo)
    k= ihi - ilo
    resta= round((bphi - bplo),1)
    print("El valor de la resta es: ",resta)
    k= round((k / resta),3)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+0.1,150.4),1)
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en Partículas Menores a 2.5 micrómetros (PM2.5) es: ", indice)


    print("\n")
    print("\n")
    print("La Calidad del Aire es MUY MALA")











"""
AQUI COMIENZA EL ULTIMO
"""

if bphi >= 0.205 and bphi  <= 0.604:
    bplo=round(random.uniform(0.205,bphi - 0.001),3)
    print("El valor de BpLo es: ", bplo)
    ihi=200
    ilo=151
    k= ihi - ilo
    resta= round((bphi - bplo),3)
    print("El valor de la resta es: ",resta)
    k= round((k / resta),2)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+0.001,0.604),3)
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en ozono es: ", indice)



    bphi=0
    bplo=0
    k=0
    resta=0
    c=0
    indice=0
    print("\n")
    print("\n")
    #SIEMPRE HAY QUE DARLE UNNO MAS
    bphi= round(random.uniform(356,604))
    print("El valor de bphi es: ", bphi)
    #bphi=40
    bplo=round(random.uniform(355,bphi - 1))
    print("El valor de bplo es: ", bplo)
    k= ihi - ilo
    resta= round((bphi - bplo))
    print("El valor de la resta es: ",resta)
    k= round((k / resta),3)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+1,604))
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en Partículas Menores a 10 micrómetros (PM10) es: ", indice)
    


    bphi=0
    bplo=0
    k=0
    resta=0
    c=0
    indice=0
    print("\n")
    print("\n")
    bphi= round(random.uniform(150.6,500.4),1)
    print("El valor de bphi es: ", bphi)
    #bphi=12.0
    bplo=round(random.uniform(150.5,bphi - 0.1),1)
    print("El valor de bplo es: ", bplo)
    k= ihi - ilo
    resta= round((bphi - bplo),1)
    print("El valor de la resta es: ",resta)
    k= round((k / resta),3)
    print("El valor de K es: ",k)
    c=round(random.uniform(bplo+0.1,500.4),1)
    print("El valor redondeado para la concentración del contaminante es: ", c)
    indice = k * (c - bplo)
    indice= round((indice + ilo))
    print("El indice de contaminación en Partículas Menores a 2.5 micrómetros (PM2.5) es: ", indice)


    print("\n")
    print("\n")
    print("La Calidad del Aire es EXTREMADAMENTE MALA")    
