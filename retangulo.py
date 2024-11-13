import cv2

# Path do arquivo jpg
img = cv2.imread(r'C:\Users\alberto\Pictures\parisjpg.jpg')

# Desenha o retângulo
cv2.rectangle(img, (30, 30), (100 + 150, 100 + 250), (0, 0, 255), 5)

# Mostra a Imagem na tela
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


