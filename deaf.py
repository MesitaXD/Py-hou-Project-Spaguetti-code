import pygame
import sys
from random import randint as aleatorio
pygame.init()
width = 800
height = 600
vida = 100
tamaño = (width, height)
window = pygame.display.set_mode(tamaño)
pygame.display.set_caption("Deaf To All But The Ronald")
frame = 1
frame_victoria = 0
numero = 0
suma_progresiva = 1
sec = 1
musica = False
vida_extra = False
daño = False
derrota = False
victoria = False
font_pequeña = pygame.font.SysFont(None, 20)
font_mediano = pygame.font.SysFont(None, 35)
font_grande = pygame.font.SysFont(None, 55)

contador = 0
clock = pygame.time.Clock()
blanco = (255, 255, 255)
negro = (0, 0, 0)
icono = pygame.image.load("images\\ran.jpg")
pygame.display.set_icon(icono)
musica = pygame.mixer.music.load("sounds\\deaf.mp3")
pygame.mixer.music.set_volume(1)
vine_sfx = pygame.mixer.Sound("sounds\\vine_boom.mp3")
pos_mouse = pygame.mouse.get_pos()
ultima_pos_mouse = pos_mouse
ultimo_movimiento = 0


sfx = False

while 1:
    if not musica:
        if not victoria:
            pygame.mixer.music.play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            if not victoria:
                if pygame.mouse.get_focused():
                    vida = 100
                    vida_extra = False
                    numero = 0
                    musica = True
                    pygame.mouse.set_pos([400, 500])
                    suma_progresiva = 1
                    sec = 1
            
    pos_mouse = pygame.mouse.get_pos()
    if pos_mouse != ultima_pos_mouse:
        ultima_pos_mouse = pos_mouse
        ultimo_movimiento = pygame.time.get_ticks()
        suma_progresiva = 1
        sec = 1
    tiempo_actual = pygame.time.get_ticks()

    diferencia = tiempo_actual - ultimo_movimiento
    if diferencia >= 1000:
        if diferencia // 2000 > sec:
            vida -= suma_progresiva
            sec += 1
            suma_progresiva = suma_progresiva*2
            contador = 60

    if frame == 1:
        vida = 100
    if frame >= 2170:
        if not vida_extra:
            vida += 200 
            vida_extra = True
            contador = 60
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if musica:
        if daño:
            contador = 60
        if vida <= 0:
            musica = False
            derrota = True

        digitos = len(str(frame))
        pygame.draw.rect(window, blanco, (0, 0, 800, 600))
        fondo = pygame.image.load("images\\deaf\\ronald"+"0"*(5-digitos)+str(frame)+".jpg").convert_alpha()
        fondo_tamaño = pygame.transform.scale(fondo, (800, 600))
        window.blit(fondo_tamaño, (0, 0))
        if frame < 4801:
            frame = int((pygame.mixer.music.get_pos())*30/1000)
        if frame == 4801:
            victoria = True
            musica = False
        if frame == 0:
            frame = 1
        if contador > 0:
            contador -= 1
            vida_a_mostrar = str(round(vida, 1))
            vida_print = font_pequeña.render(str(vida_a_mostrar) + "%", True, (0, 0, 0))
            vida_rect = vida_print.get_rect(center=(pygame.mouse.get_pos()[0] +10, pygame.mouse.get_pos()[1] - 10))
            window.blit(vida_print, vida_rect)
    pygame.display.update()

    if musica:
        if not pygame.mouse.get_focused():
            vida -= 3
        else:
            color = window.get_at(pygame.mouse.get_pos())
            if color[0] < 210 or color[1] < 210 or color[2] < 210:
                    vida -= 1
                    daño = True
            else:
                daño = False

        clock.tick(60)
    else:
        if not victoria:
            if not derrota:
                inicia = font_mediano.render('Presiona "R" mientras tienes el mouse en la pantalla para iniciar', True, negro)
                inicia_rect = inicia.get_rect(center=(width // 2, height // 2))
                pygame.draw.rect(window, blanco, (0, 0, 800, 600))
                window.blit(inicia, inicia_rect)
            else:
                if numero == 0:
                    numero = aleatorio(1, 15)
                pygame.draw.rect(window, blanco, (0, 0, 800, 600))
                derrota = font_mediano.render('Perdiste! Dale a "R" para reintentar', True, negro)
                derrota_rect = derrota.get_rect(center=(width // 2, 80))
                derrota2 = font_mediano.render('Segundos totales : ' + str(round(frame/30, 2 )), True, negro)
                derrota2_rect = derrota2.get_rect(center=(width // 2, 110))
                imagen = pygame.image.load("images\\memes\\"+str(numero)+".png").convert()
                imagen_rect = imagen.get_rect(center=(width // 2, height // 2))
                window.blit(derrota, derrota_rect)
                window.blit(derrota2, derrota2_rect)
                window.blit(imagen, imagen_rect)
        else:
            pygame.draw.rect(window, blanco, (0, 0, 800, 600))
            frame_victoria += 1
            clock.tick(60)
            image = pygame.image.load("images\\white.png")
            if frame_victoria <= 60:
                image.set_alpha(255 - frame_victoria*4.25)
            elif 60 < frame_victoria <= 170:
                image.set_alpha(0)
            elif 170 < frame_victoria < 230:
                image.set_alpha(255 - (frame_victoria-170)*4.25)
            else:
                image.set_alpha(0)

            total = 10000*vida
            puntuacion = 0
            if frame_victoria <= 70:
                puntuacion = 0
            elif 70 < frame_victoria <= 170:
                puntuacion = int((total/100)*(frame_victoria-70))
            else:
                puntuacion = total
            if vida <= 70:
                rango_letra = "f"
            elif 70 < vida <= 120:
                rango_letra = "c"
            elif 120 < vida <= 210:
                rango_letra = "b"
            elif 210 < vida < 240: 
                rango_letra = "a"
            else:
                rango_letra = "s"
            if frame_victoria > 170:
                if not sfx:
                    vine_sfx.play()
                    sfx = True
                rango_text = font_mediano.render(str(rango_letra.upper()), True, negro)
                rango_rect = rango_text.get_rect(center=(400, 120))
                rank = pygame.image.load("images\\memes\\"+str(rango_letra)+".png").convert()
                rank_rect = rank.get_rect(center=(width // 2, height // 2))
                window.blit(rango_text, rango_rect)
                window.blit(rank, rank_rect)
            victoria_text = font_mediano.render('Victoria!', True, negro)
            victoria_rect = victoria_text.get_rect(center=(400, 50))
            victoria2_text = font_mediano.render('Puntuacion : '+ str(puntuacion), True, negro)
            victoria2_rect = victoria2_text.get_rect(center=(400, 80))
            window.blit(victoria_text, victoria_rect)
            window.blit(victoria2_text, victoria2_rect)
            window.blit(image, (0, 0))