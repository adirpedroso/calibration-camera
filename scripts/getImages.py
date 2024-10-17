#Feito para criar um dataset a partir de uma camera conectada no computador
    #Caso não funcione de primeira, teste alterando a linha 6 para o valor de 2 (cap = cv2.VideoCapture(2))
    #Pressione a letra S para salvar a imagem

import cv2

cap = cv2.VideoCapture(0)

num = 0

while cap.isOpened():

    succes, img = cap.read()

    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('/home/junao99/CameraCalibration/dataset/webcam/img' + str(num) + '.png', img)
        print("image saved!")
        num += 1

    cv2.imshow('Img',img)

# Release and destroy all windows before termination
cap.release()

cv2.destroyAllWindows()