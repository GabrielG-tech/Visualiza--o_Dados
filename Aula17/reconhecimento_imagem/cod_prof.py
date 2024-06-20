import cv2  # pip install opencv-python
import time

#*  *   *   *   *   *   *   *
#*     Comparar imagens     *
#*  *   *   *   *   *   *   *
def comparar_imagens(imagem_referencia, imagem_procurada):
    orb = cv2.ORB_create()

    pontos_chave_referencia, descritores_referencia = orb.detectAndCompute(imagem_referencia, None)
    pontos_chave_procurada, descritores_procurada = orb.detectAndCompute(imagem_procurada, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(descritores_referencia, descritores_procurada)

    matches = sorted(matches, key=lambda x: x.distance)

    if len(matches) > 0:
        media_distancias = sum([match.distance for match in matches]) / len(matches)
        return media_distancias
    else:
        return None

def comp_imagem(path):
    captura = cv2.VideoCapture(1)
    imagem_referencia = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    i=0
    tempo_inicial = time.time()
    
    while True:
        ret, frame = captura.read()
        tempo_atual = time.time() 
        tempo_passado = tempo_atual - tempo_inicial  
        
        if tempo_passado >= 5:  
            return (False)
            
        if ret:
            frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            distancia_media = comparar_imagens(imagem_referencia, frame_cinza)

            if distancia_media is not None and distancia_media < 50:  # Ajuste o limite conforme necessário
                print("Imagem correspondente encontrada!" + str(i))
                i=i+1
                if(i>6):
                    return(True)

            cv2.imshow('Quadro da Webcam', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    captura.release()
    cv2.destroyAllWindows()

