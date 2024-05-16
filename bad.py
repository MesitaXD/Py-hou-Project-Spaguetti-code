import pygame
from pygame.locals import *
from pygame.sprite import Sprite
import sys
from random import randint
pygame.init()
color_jugador = "Negro"
width = 800
height = 600
tips = ("La barra naranja es un escudo! Se activa al cambiar de color", 'Si necesitas una guia, busca "Bad Apple!!!" en youtube', "Tranquilo, solo son 220 segundos", "Ouch, eso debio doler", "Intentalo denuevo, quiza esta sea la buena", "Y como va tu dia? el mio va bien", "Yyy... Eso fue incomodo de ver, sabes?", "Ya me estoy aburriendo de no verte ganar", "... Otra vez? Es enserio?", "Estoy empezando a pensar que lo haces a proposito", "A mi me prometieron una empanada si me quedaba viendote", "Tip # 12", "Sabes, ya no tengo hambre", "Hay un 6.25% de que veas esto, sabes?", "L is Real", "Mejor prueba tocar pasto! :D")
print(len(tips))
ya_tip = False
limite_izquierdo = 100 +5
limite_superior = 75 +9
limite_derecho = limite_izquierdo + 600 -9
limite_inferior = limite_superior + 450 -14
window_size = (width, height)
pausa = False
derrota = False
victoria = False
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
pygame.display.set_caption("Bad Apple!!!")
frame = 1
puntaje = 0
perfect_contador = 0
clock = pygame.time.Clock()
fps = 30
distancia = 8
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
                escudo_actual = 650
                jugador_image = pygame.image.load('images\\jugador_b_a.png').convert_alpha()
                jugador = Jugador(jugador_image, (400, 300))
                color_jugador = "Negro"
                musica.play(-1)
                ya_tip = False
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
            distancia = 4
        else:
            distancia = 8
    digitos = len(str(frame))
    if frame <= 6560:
        background_image = pygame.image.load("images\\bad\\frame"+"0"*(5-digitos)+str(frame)+".png").convert()
    elif frame > 6560:
        victoria = True
    background_image = pygame.transform.scale(background_image, (600, 450))
    window.blit(background_image, (100, 75))
    if not victoria:
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
        if avg_color >= (232, 232, 232):
            color = "Blanco"
        elif avg_color <= (90, 90, 90): 
            color = "Negro"
        else:
            color = color_jugador
        escudo_actual = max(0, escudo_actual)
        if escudo_status == True:
            escudo_actual -= escudo_max/10
            if escudo_actual <= 0:
                escudo_status = False
        else:
            if escudo_actual < escudo_max:
                escudo_actual += escudo_max/40
        if frame < 6560:
            if color != color_jugador:
                if not escudo_status:
                    vida_actual -= vida_max / tiempo_maximo_vida
    if not derrota:
        pygame.draw.rect(window, escudo_color, (80, 30, escudo_actual, 10))
        pygame.draw.rect(window, vida_color, (80, 50, vida_actual, 10))

    vida_actual = max(0, vida_actual)
    if vida_actual <= 0:    
        if not ya_tip:
            tip_numero = randint(1,len(tips))
            ya_tip = True
        perdiste_font = pygame.font.SysFont(None, 36)
        tip = perdiste_font.render(tips[tip_numero-1], True, (255, 255, 255))
        tip_rect = tip.get_rect(center=(width // 2, 55))
        perdiste_1 = perdiste_font.render("Perdiste! Presiona R para reintentar", True, (255, 255, 255))
        perdiste_2 = perdiste_font.render("Record: " + str(round(frame / 30, 1)) + " segundos", True, (255, 255, 255))
        perdiste_rect_1 = perdiste_1.get_rect(center=(width // 2, height - 55))
        perdiste_rect_2 = perdiste_2.get_rect(center=(width // 2, height - 25))
        window.blit(perdiste_1, perdiste_rect_1)
        window.blit(perdiste_2, perdiste_rect_2)
        window.blit(tip, tip_rect)
        derrota = True

    if victoria:
        background_image = pygame.image.load("images\\bad\\frame06560.png").convert()
        puntuacion_font = pygame.font.SysFont(None, 36)
        puntuacion_mensaje = puntuacion_font.render("Puntuacion = " + str(round(puntaje)), True, (255, 255, 255))
        puntuacion_rect = puntuacion_mensaje.get_rect(center=(width // 2, height // 2))
        window.blit(puntuacion_mensaje, puntuacion_rect)
        puntuacion_total = round(1000000 * (1+(vida_actual/650)))
        if puntaje < puntuacion_total:
            if frame > 6590:
                suma = round(puntuacion_total / 100, 2)
                puntaje += suma
                puntaje = round(puntaje, 2)
        if puntaje >= 2000000:
            perfect_contador += 1
            if 0 < perfect_contador < 10:
                perfect = puntuacion_font.render("NO HIT!!", True, (255, 255, 255))
                perf_rect = perfect.get_rect(center=(width // 2, height // 2 - 40))
                window.blit(perfect, perf_rect)
            elif perfect_contador == 10:
                perfect_contador = -10

    pygame.display.update()

    if not pausa:
        frame = frame + 1


    clock.tick(fps)