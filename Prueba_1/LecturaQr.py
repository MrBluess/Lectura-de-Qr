import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# Leemos la imagen del código QR
img = cv2.imread('prueba1.png')

# Convertimos la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Buscamos los códigos QR en la imagen
decoded = pyzbar.decode(gray)

# Iteramos sobre todos los códigos QR encontrados
for obj in decoded:
    # Imprimimos el tipo de código QR y su contenido
    print("Tipo de código: ", obj.type)
    print("Contenido: ", obj.data)

    # Dibujamos un rectángulo alrededor del código QR
    (x, y, w, h) = obj.rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Mostramos la imagen con los rectángulos dibujados
cv2.imshow("Imagen con códigos QR", img)
cv2.waitKey(0)
