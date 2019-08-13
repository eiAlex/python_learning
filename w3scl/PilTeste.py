# -*- coding utf-8 -*-

#  teste com pil/pillow lib de manipulação de imagens

from PIL import Image

imagemTeste = Image.open("D:\Projetos\Estudo\Python-Lerarning\-alex-kidd.jpg")

#rotaciona a imagem
imagemTeste.rotate(45)


#salava a manipulação
#imagemTeste.save('D:\Projetos\Estudo\Python-Lerarning\-alex-kidd-180.jpg')

#imprimindo o tamanho e o tipo do arquivo aberto
print(imagemTeste.size, imagemTeste.mode)