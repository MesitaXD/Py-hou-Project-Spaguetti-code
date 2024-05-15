import pygame
from pygame.locals import *
from pygame.sprite import Sprite
import sys

pygame.init()
color_jugador = "Negro"
width = 800
height = 600
limite_izquierdo = 100 +5
limite_superior = 75 +9
limite_derecho = limite_izquierdo + 600 -9
limite_inferior = limite_superior + 450 -14
window_size = (width, height)
pausa = False
derrota = False
vida_max = 650
vida_actual = 650
vida_color = (0, 255, 0)
tiempo_maximo_vida = 300
escudo_max = 650
escudo_actual = 650
escudo_color = (255, 132, 0)
escudo_status = False
color_fondo = (0, 0, 0)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Fondo Personalizado")
frame = 1
clock = pygame.time.Clock()
fps = 30
distancia = 6
ya = False
musica = pygame.mixer.Sound("sounds\\bad.mp3")
musica.play()

class Jugador(Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=position)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

jugador_image = pygame.image.load('images\\jugador_b_a.png').convert_alpha()
jugador = Jugador(jugador_image, (400, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(window, color_fondo, (0, 0, 800, 600))
    if derrota:
        pausa = True
        pygame.mixer.stop()
    if pygame.mouse.get_focused():
        pygame.mixer.unpause()
        if not derrota:
            pausa = False   
    else:
        pygame.mixer.pause()
        pausa = True
    keys = pygame.key.get_pressed()
    if keys[K_r]:
            if derrota:
                frame = 1
                vida_actual = 650
                jugador_image = pygame.image.load('images\\jugador_b_a.png').convert_alpha()
                jugador = Jugador(jugador_image, (400, 300))
                color_jugador = "Negro"
                musica.play(-1)
                derrota = False
    if not pausa:
        if keys[pygame.K_UP]:
            if jugador.rect.top > limite_superior:
                jugador.rect.y -= distancia
        if keys[pygame.K_DOWN]:
            if jugador.rect.bottom < limite_inferior:
                jugador.rect.y += distancia
        if keys[pygame.K_LEFT]:
            if jugador.rect.left > limite_izquierdo:
                jugador.rect.x -= distancia
        if keys[pygame.K_RIGHT]:
            if jugador.rect.right < limite_derecho:
                jugador.rect.x += distancia
        if keys[K_z]:
            escudo_status = True
            if not ya:
                if color_jugador == "Negro":
                    color_jugador = "Blanco"
                    jugador_image = pygame.image.load('images\\jugador_b_b.png').convert_alpha()
                    jugador = Jugador(jugador_image, (jugador_x, jugador_y))
                elif color_jugador == "Blanco":
                    color_jugador = "Negro"
                    jugador_image = pygame.image.load('images\\jugador_b_a.png').convert_alpha()
                    jugador = Jugador(jugador_image, (jugador_x, jugador_y))
                    
                ya = True
        elif not keys[K_z]:
            ya = False
        if keys[K_LSHIFT]:
            distancia = 2
        else:
            distancia = 6
    digitos = len(str(frame))
    background_image = pygame.image.load("images\\bad\\frame"+"0"*(5-digitos)+str(frame)+".png").convert()
    background_image = pygame.transform.scale(background_image, (600, 450))
    window.blit(background_image, (100, 75))
    jugador.draw(window)
    jugador_rect = jugador.rect
    jugador_x = jugador_rect.x +10
    jugador_y = jugador_rect.y +10
    if not pausa:
        area_color_sum = [0, 0, 0]
        num_pixels = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                x = jugador_x + dx
                y = jugador_y + dy
                color = window.get_at((x, y))
                area_color_sum[0] += color[0]
                area_color_sum[1] += color[1]
                area_color_sum[2] += color[2]
                num_pixels += 1
        avg_color = (area_color_sum[0] // num_pixels, area_color_sum[1] // num_pixels, area_color_sum[2] // num_pixels)
        if avg_color >= (130, 130, 130):
            color = "Blanco"
        elif avg_color <= (120, 120, 120): 
            color = "Negro"
        escudo_actual = max(0, escudo_actual)
        if escudo_status == True:
            escudo_actual -= escudo_max/10
            if escudo_actual <= 0:
                escudo_status = False
        else:
            if escudo_actual < escudo_max:
                escudo_actual += escudo_max/40
        print(escudo_status)
        if color != color_jugador:
            if not escudo_status:
                vida_actual -= vida_max / tiempo_maximo_vida
    pygame.draw.rect(window, escudo_color, (80, 30, escudo_actual, 10))
    pygame.draw.rect(window, vida_color, (80, 50, vida_actual, 10))
    
    vida_actual = max(0, vida_actual)
    if vida_actual <= 0:
        perdiste_font = pygame.font.SysFont(None, 36)
        perdiste_1 = perdiste_font.render("Perdiste! Presiona R para reintentar", True, (255, 255, 255))
        perdiste_2 = perdiste_font.render("Record: " + str(round(frame / 30, 1)) + " segundos", True, (255, 255, 255))
        perdiste_rect_1 = perdiste_1.get_rect(center=(width // 2, height - 55))
        perdiste_rect_2 = perdiste_2.get_rect(center=(width // 2, height - 25))
        window.blit(perdiste_1, perdiste_rect_1)
        window.blit(perdiste_2, perdiste_rect_2)
        derrota = True
    pygame.display.update()

    if not pausa:
        frame = frame + 1


    clock.tick(fps)