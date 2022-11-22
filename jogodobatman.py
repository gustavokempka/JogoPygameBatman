import os
import pygame
import time
pygame.init()
os.system("cls")
print("Começando a Jornada!")
largura = 1366
altura = 768
tamanho = (largura,altura) 
display = pygame.display.set_mode( tamanho )
fps = pygame.time.Clock()
pygame.display.set_caption("Batman")
branco = (255,255,255)
preto = (0,0,0)
cor = (170,50,8) 
jogando = True

esgoto = pygame.image.load("jogodobatman/gothamcity.jpg")
batman = pygame.image.load("jogodobatman/batmansoco.png")
batman = pygame.transform.scale(batman, (200, 200)) 
crocodilo = pygame.image.load("jogodobatman/crocodilo.png")
crocodilo = pygame.transform.scale(crocodilo, (300,300))
chao = pygame.image.load("jogodobatman/chao.png")
manbat = pygame.image.load("jogodobatman/manbat.png")
manbat = pygame.transform.scale(manbat, (290,290))

tamanhoXBatman = 50
tamanhoYBatman = 50
posicaoBatmanX = 10
posicaoBatmanY = 560
movimentoBatmanX = 0
movimentoBatmanY = 0
velocidade = 10


pygame.mixer.music.load("jogodobatman/trilhasonora.wav")
pygame.mixer.music.play(1)
soco = pygame.mixer.Sound("jogodobatman/soco.wav")

def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,branco)
    display.blit(textoDisplay, (5,5))

def pontuou ():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(soco)
    fonte  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("Você Venceu!",True,branco)
    display.blit(textoDisplay, (260,90))
    pygame.display.update()
    time.sleep(3)
    pygame.mixer.music.load("jogodobatman/ganhou.wav")
    pygame.mixer.music.play(1) 
    pygame.mixer.music.set_volume(1) 
    pygame.mixer.music.load("jogodobatman/trilhasonora.wav")
    pygame.mixer.music.play(1)




while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimentoBatmanX = velocidade * -1
            elif evento.key == pygame.K_RIGHT:
                movimentoBatmanX = velocidade
            elif evento.key == pygame.K_UP:
                movimentoBatmanY = velocidade * -1
            elif evento.key == pygame.K_DOWN:
                movimentoBatmanY = velocidade
        elif evento.type == pygame.KEYUP:
            movimentoBatmanX = 0
            movimentoBatmanY = 0
    
    
    if posicaoBatmanX + movimentoBatmanX + tamanhoXBatman < largura and posicaoBatmanX + movimentoBatmanX > 0:
        posicaoBatmanX = posicaoBatmanX + movimentoBatmanX

    if posicaoBatmanY +movimentoBatmanY + tamanhoYBatman < altura and posicaoBatmanY + movimentoBatmanY > 0:
        posicaoBatmanY = posicaoBatmanY + movimentoBatmanY

    display.fill(branco)
    display.blit(esgoto , (0,0) )
    posicao = (posicaoBatmanX,posicaoBatmanY) 
    display.blit(chao, (100,600))
    display.blit(chao, (50,600))
    display.blit(chao, (0,600))
    display.blit(chao, (300,600))
    display.blit(chao, (400,600))
    display.blit(chao, (500,600))
    display.blit(chao, (600,600))
    display.blit(chao, (700,600))
    display.blit(chao, (800,600))
    display.blit(chao, (200,600))
    display.blit(chao,(1000,600))
    display.blit(chao, (1200,600))
    display.blit(batman , (posicaoBatmanX,posicaoBatmanY) )
    display.blit(crocodilo , (1000,485))
    display.blit(manbat , (1000,10))
    

    if posicaoBatmanY > 0 and posicaoBatmanX> 173 and posicaoBatmanX > 990:
        pontuou()
        posicaoBatmanX = 0
        posicaoBatmanY = 560
        
    pygame.display.update()
    fps.tick(60)
