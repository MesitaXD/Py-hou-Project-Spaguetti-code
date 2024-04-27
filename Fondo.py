import pygame
import pgzrun
import math

from random import randint
WIDTH = 800
HEIGHT = 600
activa = False
focus = False
primera_vez = 0
bomb_type = 2
tiempo_inicial_tecla = 0
eee = True
daño_golpe = 3
suma_1 = 8
suma_2 = -8
bomba_print = False
espera_nojoda = 0
daño = 0

rotation = False
bubble  = False
bomba_cd = False
numero = 0
angulo_aumento = 0
fondito = "fondo_menu.png"  
jugador = Actor('jugador.jpg', (200, 530))
hitbox = Actor('hitbox', (200, 530))
death_hitbox = Actor("hitbox.jpg", (200, 430))
contador = 0
contador_enemigo = 0
bomba_2 = []
espera = 5
espera_enemigos = 5
balas = []
enemigos = []
enemigo_spawn = True
rango_visible = Actor("cubo_visible.jpg", (205, 300))
atacante = Actor("jugador.jpg", (195, 90))
wawa = Actor("no_evidence.png", (5000, 300))
bala_circular = []
circulos_wa = []
aleatorio = 0
contador_enemigo_2 = 0
contador_enemigo_3 = 0
numero_2 = 0
vida_max = 320
vida_verde =  Rect((65, 20), (vida_max, 10))




def draw():

    rango_visible.draw()
    for cosa in bala_circular:
        cosa[0].draw()

    for cosa in circulos_wa:
        cosa[0].draw()

    if bomba_print:
        if bomb_type == 1:
            wawa.draw()
        if bomb_type == 2:
            for burbuja in bomba_2:
                burbuja[0].draw()
    
    screen.blit(fondito, (0, 0))

    screen.draw.rect(vida_verde, (0, 255, 0))
    screen.draw.filled_rect(vida_verde, (0, 255, 0))
    for enemigo in enemigos:
        enemigo[0].draw()

    if focus == True:
        jugador.draw()
        hitbox.draw()
    else:
        jugador.draw()
    death_hitbox.draw()
    atacante.draw()

    for bala in balas:
        bala.draw()





def update():
    global bomba_cd
    direccion = ""
    if (keyboard.up):
        direccion = 'up'
        mover_jugador(direccion)
    if (keyboard.down):
        direccion = 'down'
        mover_jugador(direccion)
    if (keyboard.left) :
        direccion = 'left'
        mover_jugador(direccion)
    if (keyboard.right) :
        direccion = 'right'
        mover_jugador(direccion)
    if keyboard.q:
        spawn_enemigos(True)

    if (keyboard.z):
        disparo(True)

    if (keyboard.e):
        bala_circulos("si")
    else:
        bala_circulos("no")

    if (keyboard.lshift):
        global focus
        focus = True
    else:
        focus = False
        
    if rotation == True:
        numero = 0
        global bomba_print
        global angulo_aumento
        bomba_print = True
        wawa.x = 205
        for a in range(720):
            numero += 1
            if numero == 100:
                if angulo_aumento < 15:
                    angulo_aumento += 0.1
                wawa.angle += angulo_aumento
    else:
        angulo_aumento = 0
        wawa.angle = 0
        wawa.x = 5000
        bomba_print = False

    if bubble == True:
        global primera_vez
        bomba_print = True
        if primera_vez == 0:
            bomba_print = True
            coord = jugador.pos
            burbuja_1 = Actor("explosive_mix.png", coord)
            burbuja_2 = Actor("explosive_mix.png", coord)
            b1 = (burbuja_1, 1)
            b2 = (burbuja_2, 2)
            bomba_2.append(b1)
            bomba_2.append(b2)
            primera_vez = 1
    else: 
        primera_vez = 0
        
    for burbuja in bomba_2:
        global suma_1
        global suma_2
        if burbuja[1] == 1:
            burbuja[0].y -= 1
            if (burbuja[0].x <= 31):
                suma_1 = 8
            if (burbuja[0].x >= 379):
                suma_1 = -8
            burbuja[0].x += suma_1
        elif burbuja[1] == 2:
            burbuja[0].y -= 1
            if (burbuja[0].x <= 31):
                suma_2 = 8
            if (burbuja[0].x >= 379):
                suma_2= -8
            burbuja[0].x += suma_2

    if keyboard.a:
        bala_spin(True)
    else:
        bala_spin(False)

    if keyboard.x:
        if not bomba_cd:
            global activa
            activa = True
    
    if activa == True:
        global espera_nojoda
        espera_nojoda += 1
        if bomb_type == 1:
            espera = 300
        if bomb_type == 2:
            espera = 600    

        if espera_nojoda <= espera:
            bomba_cd = True
            bomba(True)
            print (espera_nojoda)
        else:
            bomba_cd = False
            activa = False 
            espera_nojoda = 0
            bomba(False)


    for bala in balas:
        global vida_max, vida_verde, daño, daño_golpe
        bala.y -= 10
        verificar_rango(bala)
        if bala.colliderect(death_hitbox):
            balas.remove(bala)
            death_hitbox.x += randint(-10, 10)
        if bala.colliderect(atacante):
            daño +=1
            print ("ENEMIGO GOLPEADO")
            print (daño)
            balas.remove(bala)
            if daño == daño_golpe:
                daño = 0
                vida_max -= 10
                vida_verde = Rect((65, 20), (vida_max, 10))

    if vida_max > 160:
        bala_spin(True)
    if 70 < vida_max <=160:
        bala_circulos("si")
        movimiento_rival(True)
    if vida_max <= 70:
        daño_golpe_cambio(25)

    for cosa in bala_circular:

        cosa[0].y += 5 * cosa[1][1]
        cosa[0].x += 5 * cosa[1][0]

    for cosa in circulos_wa:

        cosa[0].y += 5 * cosa[1][1]
        cosa[0].x += 5 * cosa[1][0]

    for enemigo in enemigos:    

        if hitbox.colliderect(enemigo[0]):
            print("GOLPE")
        
        enemigo[0].y += 5 * enemigo[1][1]
        enemigo[0].x += 5 *enemigo[1][0]

        for bala in balas:
            if enemigo[0].colliderect(bala):
                if enemigo in enemigos:
                    enemigos.remove(enemigo)
                    balas.remove(bala)
        
        if (enemigo[0].y <= 26):
            if enemigo in enemigos:
                    enemigos.remove(enemigo)
        if (enemigo[0].x <= 31):
            if enemigo in enemigos:
                    enemigos.remove(enemigo)
        if (enemigo[0].y >= 574):
            if enemigo in enemigos:
                    enemigos.remove(enemigo)
        if (enemigo[0].x >= 379):
            if enemigo in enemigos:
                    enemigos.remove(enemigo)

    for coso in bala_circular:   
        if not coso[0].colliderect(rango_visible):
            bala_circular.remove(coso)
        if coso[0].colliderect(wawa):
            if coso in bala_circular:
                bala_circular.remove(coso)
        for burbuja in bomba_2:
            if coso[0].colliderect(burbuja[0]):
                if coso in bala_circular:
                    bala_circular.remove(coso)
                

    for coso in circulos_wa:   
        if not coso[0].colliderect(rango_visible):
            circulos_wa.remove(coso)
        if coso[0].colliderect(wawa):
            if coso in circulos_wa:
                circulos_wa.remove(coso)    
        for burbuja in bomba_2:
            if coso[0].colliderect(burbuja[0]):
                if coso in circulos_wa:
                    circulos_wa.remove(coso)




def mover_jugador(direccion, distancia = 4):

    if (keyboard.lshift):
        distancia = 1.7
    if (direccion == 'up'):
        jugador.y -= distancia
        hitbox.y -= distancia
    if (direccion == 'right'):
        jugador.x += distancia
        hitbox.x += distancia
    if (direccion == 'down'):
        jugador.y += distancia
        hitbox.y += distancia
    if (direccion == 'left'):
        jugador.x -= distancia
        hitbox.x -= distancia

    if (jugador.y <= 26):
        jugador.y = 26
        hitbox.y = 26
    if (jugador.x <= 31):
        jugador.x = 31
        hitbox.x = 31
    if (jugador.y >= 574):
        jugador.y = 574
        hitbox.y = 574
    if (jugador.x >= 379):
        jugador.x = 379
        hitbox.x = 379

def disparo(disparo):
    global contador
    if focus == False:
        if disparo == True:
            contador += 1
            if contador == espera:
                contador = 0
                bala = Actor('hitbox', (jugador.x, jugador.y - 9))
                balas.append(bala)
    else:
        if disparo == True:
            contador += 1
            if contador == espera:
                contador = 0
                bala = Actor('hitbox', (jugador.x, jugador.y - 9))
                bala_2 = Actor('hitbox', (jugador.x + 15, jugador.y - 9))
                bala_3 = Actor('hitbox', (jugador.x - 15, jugador.y - 9))
                balas.append(bala)
                balas.append(bala_2)
                balas.append(bala_3)


def spawn_enemigos(enemigo):
    global contador_enemigo
    if enemigo == True:
        contador_enemigo += 1
        if contador_enemigo == espera_enemigos - 2:
            contador_enemigo = 0
            aleatorio = randint(45, 135)
            malo = Actor("jugador.jpg", (randint(31, 378), 26))
            trayectoria = seno_random(aleatorio)
            duo = (malo, trayectoria)
            enemigos.append(duo)

def verificar_rango(objeto):
    if not rango_visible.colliderect(objeto):
        if objeto in balas:
            balas.remove(objeto)
        if objeto in enemigos:
            enemigos.remove(objeto)

def seno_random(valor):
    y = math.sin(math.radians(valor))
    if valor > 90:
        x = 1 - y
    elif valor < 90:
        x =  (-y + 1)*-1
    else:
        x = 0 
    return round(x, 2), round(y, 2)


def bala_spin(a):
    global numero
    global contador_enemigo
    if a == True:
        contador_enemigo += 1
        if contador_enemigo == espera_enemigos - 2:
            contador_enemigo = 0
            for random in range(0, 360, 60):
                nuevo = numero + random
                y = math.sin(math.radians(nuevo))
                x = math.cos(math.radians(nuevo))
                coord = (x, y)
                balas = Actor("bala.png", atacante.pos)
                todo = (balas, coord)
                bala_circular.append(todo)
            numero += 14

def bala_circulos(e):
    global numero_2
    global contador_enemigo_3
    if e == "si":
        contador_enemigo_3 += 1
        if contador_enemigo_3 == 4:
            contador_enemigo_3 = 0
            for a in range(18):
                numero_2 += 20
                y = math.sin(math.radians(numero_2))
                x = math.cos(math.radians(numero_2))
                coord = (x, y)
                bala = Actor("bala.png", atacante.pos)
                todo = (bala, coord)
                circulos_wa.append(todo)
            
def movimiento_rival(wa):
    global contador_enemigo_2
    global aleatorio
    global atacante
    global eee
    random = 0
    if eee == True:
        atacante.x = 145
        eee = False
    if wa == True:
        contador_enemigo_2 += 1
        if contador_enemigo_2 == 2:
            contador_enemigo_2 = 0
            random += 10
            if random == 360:
                random = 0
            aleatorio += random
            x = math.sin(math.radians(aleatorio))
            y = math.cos(math.radians(aleatorio*3))
            atacante.x += 15*x
            atacante.y += 6*y

def bomba(a):
    global rotation
    global bubble
    if bomb_type == 1:
        if a == True:
            rotation = True
        else:
            rotation = False
    if bomb_type == 2:
        if a == True:
            bubble = True
        else:
            bubble = False


def daño_golpe_cambio(entero: int):
    global daño_golpe
    daño_golpe = entero
        


pgzrun.go()