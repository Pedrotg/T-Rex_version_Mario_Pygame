# -*- coding: utf-8 -*-
import sys, pygame as py
from pygame.locals import *
import schedule as sch
import time

#variables globales
ancho = 650
alto = 450

xixf = {}

#datos de inicio de los personajes
#Mario quito
marioAncho = 29
marioAlto = 40
coordenadaXMario = 100
coordenadaYMario = 253

#Mario salta
marioSaltaAncho = 34
marioSaltaAlto = 34
coordenadaXMarioSalta = 100
coordenadaYMarioSalta = 253

coordenadaXBrowser = 510
coordenadaYBrowser = 245

coordenadaXFlama = 680
coordenadaYFlama = 258
imagenFlamaAncho = 35
imagenFlamaAlto = 12

flamaActivada = False
flamaVisible = False

pausa = False

puntaje = "0"
apareceTextoreiniciar = "Presiona R para reiniciar el juego"

def reiniciar():
    global flamaActivada, flamaVisible, puntaje, marioAncho,marioAlto,coordenadaXMario,coordenadaYMario,marioSaltaAncho,marioSaltaAlto,coordenadaXMarioSalta,coordenadaYMarioSalta,coordenadaXBrowser,coordenadaYBrowser,coordenadaXFlama,coordenadaYFlama,imagenFlamaAncho, imagenFlamaAlto, pausa

    puntajeSuma = int(puntaje)
    puntajeSuma *= 0
    puntaje = str(puntajeSuma)

    flamaActivada = False
    flamaVisible = False
    marioAncho = 29
    marioAlto = 40
    coordenadaXMario = 100
    coordenadaYMario = 253
    marioSaltaAncho = 34
    marioSaltaAlto = 34
    coordenadaXMarioSalta = 100
    coordenadaYMarioSalta = 253
    coordenadaXBrowser = 510
    coordenadaYBrowser = 245
    coordenadaXFlama = 680
    coordenadaYFlama = 258
    imagenFlamaAncho = 35
    imagenFlamaAlto = 12
    pausa = False
    main()

def activarLlama():
    global flamaActivada, flamaVisible
    flamaActivada = True
    flamaVisible = True

def sprite():

    global cont
    global contador 
    
    xixf[0] = (100,273,50,50) #posición inicial de Browser boca cerrada
    xixf[1] = (0,273,50,50) #posición inicial de Browser boca abierta

def main():

    #bucle
    terminado = False
    #variables globales
    global flamaActivada, flamaVisible, puntaje, marioAncho,marioAlto,coordenadaXMario,coordenadaYMario,marioSaltaAncho,marioSaltaAlto,coordenadaXMarioSalta,coordenadaYMarioSalta,coordenadaXBrowser,coordenadaYBrowser,coordenadaXFlama,coordenadaYFlama,imagenFlamaAncho,imagenFlamaAlto, pausa, apareceTextoreiniciar
    
    #crea ventana
    ventana = py.display.set_mode((ancho,alto))
    py.key.set_repeat(1,25)
    reloj = py.time.Clock()

    #crea fondo
    imagenFondo = py.image.load("/Users/pedrotrujillogarcia/Documents/Python/DinoPoo/Img/fondo2.jpg") 
    imagenFondo = py.transform.scale(imagenFondo,(ancho, alto))
    
    #crea personaje Mario quieto
    imagenMario = py.image.load("/Users/pedrotrujillogarcia/Documents/Python/DinoPoo/Img/marioq.png")
    imagenMario = py.transform.scale(imagenMario,(marioAncho, marioAlto))
    rectanguloMario = imagenMario.get_rect()
    rectanguloMario.left = coordenadaXMario
    rectanguloMario.top = coordenadaYMario
    marioSaltando = False
    marioBaja = False

    #crea personaje Mario salta
    imagenMarioS = py.image.load("/Users/pedrotrujillogarcia/Documents/Python/DinoPoo/Img/marios.png")
    imagenMarioS = py.transform.scale(imagenMarioS,(marioSaltaAncho, marioSaltaAlto))
    rectanguloMarioS = imagenMarioS.get_rect()
    rectanguloMarioS.left = coordenadaXMarioSalta
    rectanguloMarioS.top = coordenadaYMarioSalta
    
    #crea personaje Browser
    imagenBrowser = py.image.load("/Users/pedrotrujillogarcia/Documents/Python/DinoPoo/Img/enemigos.png")
    rectanguloBrowser = imagenBrowser.get_rect()
    rectanguloBrowser.left = coordenadaXBrowser
    rectanguloBrowser.top = coordenadaYBrowser
   
    #crea flama
    imagenFlama = py.image.load("/Users/pedrotrujillogarcia/Documents/Python/DinoPoo/Img/flama.png")
    imagenFlama = py.transform.scale(imagenFlama,(imagenFlamaAncho, imagenFlamaAlto))
    rectanguloFlama = imagenFlama.get_rect()
    rectanguloFlama.left = coordenadaXFlama
    rectanguloFlama.top = coordenadaYFlama
    flamaFinal = False

    #creamos tiempo para accionar cada 3 segundos
    sch.every(3).seconds.do(activarLlama)
    #llamaCiclo = Scheduler()
    #llamaCiclo.add(3, 0, activarLlama)

    while not terminado:
        #método de prite
        sprite()
        #realizar la tarea por tiempo
        if rectanguloFlama.left == 680 and not flamaActivada and not pausa:
            sch.run_pending() #Controlar llama
            #if rectanguloFlama.left < 680:
                #sch.clear()

        #Acción del teclado
        if not pausa:
            keys = py.key.get_pressed()

        if keys[K_UP] and not marioSaltando:
            marioSaltando = True

        #agrega imagen a la ventana
        ventana.blit(imagenFondo, (0, 0))

        #crea texto puntaje
        tipoLetra = py.font.Font("freesansbold.ttf", 32)
        textoVidas = tipoLetra.render(puntaje ,True, (255, 255, 255))
        rectanguloVidas = textoVidas.get_rect()
        rectanguloVidas.center = (510, 40)
        ventana.blit(textoVidas, rectanguloVidas)

        #crea texto puntaje
        tipoLetraReinicia = py.font.Font("freesansbold.ttf", 30)
        textoReiniciar = tipoLetraReinicia.render(apareceTextoreiniciar ,True, (255, 255, 255))
        rectanguloReiniciar = textoReiniciar.get_rect()
        rectanguloReiniciar.center = ((ancho/2), (alto/2))

        if flamaActivada:
            
            if rectanguloFlama.colliderect(rectanguloMario) or rectanguloFlama.colliderect(rectanguloMarioS):
                ventana.blit(textoReiniciar, rectanguloReiniciar)
                py.display.update()

                while not pausa:
                    for event in py.event.get():
                        if event.type==KEYUP:
                            if event.key==K_r:
                                pausa = True
                                reiniciar()

            else:
                if rectanguloFlama.right == 75:
                    apareceTextoFin = False
                    puntajeSuma = int(puntaje)
                    puntajeSuma += 1
                    puntaje = str(puntajeSuma)

            rectanguloFlama.left -= 10
            if rectanguloFlama.left <= -40:
                flamaFinal = True

            if flamaVisible:
                rectanguloFlama.left = 490
                flamaVisible = False

            if flamaFinal:                
                rectanguloFlama.left = coordenadaXFlama
                flamaFinal = False
                flamaActivada = False
                
            ventana.blit(imagenFlama, rectanguloFlama)
            ventana.blit(imagenBrowser,rectanguloBrowser, (xixf[1]))

        else:
            ventana.blit(imagenBrowser,rectanguloBrowser, (xixf[0]))

        if marioSaltando:
            if not marioBaja:
                rectanguloMario.top -= 12
                rectanguloMarioS.top -= 12
                
            if marioBaja:
                rectanguloMario.top += 12
                rectanguloMarioS.top += 12

            if rectanguloMarioS.top <= 155:
                marioBaja = True

            if rectanguloMarioS.top == 253:
                marioBaja = False
                marioSaltando = False
            
            ventana.blit(imagenMarioS, rectanguloMarioS)
        else:
            ventana.blit(imagenMario, rectanguloMario)

        #Mostrar la ventana
        py.display.flip()
        
        #cerrar ventana
        for eventos in py.event.get():
            if eventos.type == QUIT: 
                terminado = True
                py.quit()
                sys.exit(0)
        
        reloj.tick(40)

if __name__ == "__main__":
    py.init()
    main()