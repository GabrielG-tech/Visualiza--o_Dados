#pip install opencv-python

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao abrir a câmera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Erro ao capturar o frame.")
        break

    cv2.imshow('Captura de Imagem', frame)
    
    key= cv2.waitKey(1)
    
    if key == ord('q'):
        break

cv2.imwrite ('captura_de_imagem.png', frame)
print ("Imagem capturada e salva como 'captura_de_imagem.png'.")

cap.release()
cv2.destroyAllWindows()
