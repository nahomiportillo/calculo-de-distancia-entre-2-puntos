punto1x = ''
punto1y = ''
punto2x = ''
punto2y = ''


def distancia(x1,y1,x2,y2):
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        d = ((x1 - x2)**2 + (y1-y2)**2)**0.5
        return "La distancia es de: " + str(d)
    except:
        return "Error, no se puede realizar este calculo"

while True:
    print('''
    ------------------Calculo de distancia entre puntos------------------
    ''')
    punto1x = input('Ingrese la cordenada X del primer punto: ')
    punto1y = input('Ingrese la cordenada Y del primer punto: ')
    punto2x = input('Ingrese la cordenada X del segundo punto: ')
    punto2y = input('Ingrese la cordenada Y del segundo punto: ')
    dist = distancia(punto1x,punto1y,punto2x,punto2y)
    print(dist)
    input('Presione ester para continuar...')


