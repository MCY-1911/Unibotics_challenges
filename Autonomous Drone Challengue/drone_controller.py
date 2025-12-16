import WebGUI
import HAL
import Frequency
import math
import cv2
import cv2.data
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

height = 3
is_there = False
x, y, z = HAL.get_position()
x_frenada = 17
y_frenada = -17
x_objetivo = 36
y_objetivo = -35
survivors = set()


alfa = 0
a = 1
b = 2
incremento_alfa = math.pi * 2 / 16
r = 0
angles = [0, 45, 90, 135, 180, 225, 270, 315, 360]
distancia_minima = 3.0

def get_distancia(p1, p2):
    """Calcula la distancia euclidiana entre dos puntos (tuplas)."""
    return math.dist(p1,p2)

def anadir_punto_si_lejos(conjunto_puntos, nuevo_punto):
    """
    Añade 'nuevo_punto' al 'conjunto_puntos' si está a más de 'umbral_distancia'
    de cualquier punto existente.
    """
    # Si el conjunto está vacío, siempre se añade el punto
    if not conjunto_puntos:
        conjunto_puntos.add(nuevo_punto)
        return True

    # Verificar la distancia a todos los puntos existentes
    for punto_existente in conjunto_puntos:
        if get_distancia(nuevo_punto, punto_existente) < distancia_minima:
            return False # Está demasiado cerca de al menos uno

    # Si llega aquí, está lo suficientemente lejos de todos
    conjunto_puntos.add(nuevo_punto)
    return True

HAL.takeoff(height)
while True:
    Frequency.tick()

    WebGUI.showImage(HAL.get_ventral_image())

    while not is_there:
        x, y, z = HAL.get_position()
        err_z = height - z
        HAL.set_cmd_vel(15, -15, err_z, 0)
        WebGUI.showImage(HAL.get_ventral_image())
        if x > x_frenada and y < y_frenada:
            is_there = True
            HAL.set_cmd_vel(0, 0, 0, 0)
            break

    print("¡Centrandonos en el presidente!")
    x, y, z = HAL.get_position()
    distancia = math.dist((x,y),(x_objetivo,y_objetivo))
    while distancia < 0.5:
        HAL.set_cmd_pos(x_objetivo, y_objetivo, 3, HAL.get_yaw())
    
    while r < 12: 
        WebGUI.showImage(HAL.get_ventral_image())
        r = a + b * (alfa) / (2 * math.pi)
        x_target = x_objetivo + r * math.cos(alfa)
        y_target = y_objetivo + r * math.sin(alfa)
        x, y, z = HAL.get_position()
        distancia = math.dist((x,y),(x_target,y_target))
        while distancia > 0.5:
            image = HAL.get_ventral_image()
            WebGUI.showImage(image)
            x, y, z = HAL.get_position()
            distancia = math.dist((x,y),(x_target,y_target))
            HAL.set_cmd_pos(x_target, y_target, height, 0)
        alfa += incremento_alfa
        image = HAL.get_ventral_image()
        WebGUI.showImage(image)
        for angle in angles:
            altura, anchura = image.shape[:2]
            centroRotacion = (anchura / 2, altura / 2)
            matrizRotacion = cv2.getRotationMatrix2D(centroRotacion, angle, 1)
            ventralRotada = cv2.warpAffine(image, matrizRotacion, (anchura, altura))
            grisRotada = cv2.cvtColor(ventralRotada, cv2.COLOR_BGR2GRAY)
            WebGUI.showLeftImage(grisRotada)
            faces = faceCascade.detectMultiScale(grisRotada, scaleFactor = 1.02, minNeighbors = 2)
            for i in range(len(faces)):
                x, y, z = HAL.get_position()
                anadir_punto_si_lejos(survivors, (x, y))

    break

print("Volviendo a casa")
print(f"Survivors totales: {len(survivors)}")  

x, y, z = HAL.get_position()
while get_distancia((x,y), (0,0)) > 0.5:
    HAL.set_cmd_pos(0, 0, 3, HAL.get_yaw())
    x, y, z = HAL.get_position()

HAL.land()
print("Rescate completado")
print(f"Survivors totales: {len(survivors)}")    
print(survivors)



    
    
    


