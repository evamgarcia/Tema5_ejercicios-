import sys
nuevo_fichero = open("contador.txt", "a+")
nuevo_fichero.seek(0)
informacion = nuevo_fichero.readline()
if len(informacion) == 0:
    informacion = "0"
    nuevo_fichero.write(informacion)
nuevo_fichero.close()
try:
    contador = int(informacion)
    if len(sys.argv)==2:
        if sys.argv[1]=="inc":
            contador += 1
        elif sys.argv[1]== "dec":
            contador -=1
        print(contador)
        nuevo_fichero = open("contador.txt", "w")
        nuevo_fichero.write(str(contador))
        nuevo_fichero.close()
except:
    print("Error: Fichero corrupto")
