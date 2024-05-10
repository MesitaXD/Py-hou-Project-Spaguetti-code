import os
import tkinter as tk
from tkinter import messagebox as mensaje
mensaje = tk.Tk()
mensaje.title("Build")
mensaje.geometry("200x130+560+240")
mensaje.configure(bg="#f0f0f0") 
nueva_build = 1
def crear_build(text):
    global nueva_build
    if text == "1":
        nueva_build = 1
    elif text == "2":
        nueva_build = 2
    else:
        nueva_build = 3
    label.config(text=str(nueva_build))
def cerrar_ventana():
    mensaje.destroy()


boton_estilo = {
    "font": ("Times News Roman", 12),  
    "fg": "white",    
    "relief": "raised",
}

boton1 = tk.Button(mensaje, text="BUILD 1", command=lambda: crear_build("1"), **boton_estilo, bg="#FF0000", activebackground="#550000", activeforeground="White")
boton2 = tk.Button(mensaje, text="BUILD 2", command=lambda: crear_build("2"), **boton_estilo, bg="#00A2E8", activebackground="#005D85", activeforeground="White")
boton3 = tk.Button(mensaje, text="BUILD 3", command=lambda: crear_build("3"), **boton_estilo, bg="#22B14C", activebackground="#125C27", activeforeground="White")

boton1.grid(row=1, column=0, padx=10, pady=5)
boton2.grid(row=2, column=0, padx=10, pady=5)
boton3.grid(row=3, column=0, padx=10, pady=5)

cerrar = tk.Button(mensaje, text="Escojer", command=cerrar_ventana, **boton_estilo, bg="#6764B1", activebackground="#37355E", activeforeground="White")
cerrar.grid(row=3, column=1, padx=16, pady=5)

label = tk.Label(mensaje, text=str(nueva_build), font=("Arial", 18), bg="#f0f0f0")
label.grid(row=2, column=1, padx=20, pady=5)

mensaje.mainloop()

os.environ['SDL_VIDEO_WINDOW_POS'] = '460,140'
import pygame
import pgzrun
import math
import sys
from random import randint
WIDTH = 800
HEIGHT = 600
activa = False
focus = False
primera_vez = 0
build = 0
bomba_y_vida = False
tiempo_inicial_tecla = 0
eee = True
invencibilidad = False
numero_pa_eliminar_bomba = 0
numero_pa_eliminar_vida = 0
daño_golpe = 5
suma_1 = 8  
suma_2 = -8
aumento_nuclear = 5
bomba_print = False
espera_nojoda = 0
daño = 0
primera_bomba = 0
rotation = False
bubble  = False
nuclear = False
bomba_activada = False
segundo = 0
contador_explosion = 0
bomba_cd = False
numero = 0
angulo_aumento = 0
fondito = "fondo_menu.png"  
jugador = Actor('jugador.jpg', (200, 530))
hitbox = Actor('hitbox.png', (200, 530))
gracia = Actor('graze_semi.png', (jugador.x, jugador.y))
menu_pausa = Actor('pausa.png', (-163, 300))
vel_build = 0
shift_build = 0
lista_graciados = []
contador = 0
contador_extra = 0
contador_enemigo = 0
bomba_2 = []
bomba_3 = Actor("nuclear.png", (5000, 300))
espera_bala = 0
espera = 0
espera_extra = 0
espera_enemigos = 5
balas = []
teledirigidas = []
teledirigido_ex = []
tele_x = 0
tele_y = 0
hipo = 0
mov_x = 0
mov_y = 0
enemigos = []
enemigo_spawn = True
rango_visible = Actor("cubo_visible.jpg", (205, 300))
atacante = Actor("jugador.jpg", (195, 90))
bomba_1 = Actor("no_evidence.png", (1, 1))
bala_circular = []
circulos_wa = []
aleatorio = 0
contador_enemigo_2 = 0
contador_enemigo_3 = 0
numero_2 = 0
vida_max = 320
numero_vidas = []
numero_bombas = []
vida_verde =  Rect((65, 20), (vida_max, 10))
numero_de_bombas = 0
primera_vez_rotacion = 0
posicion_x = 0
posicion_y = 0
diferencia_x = 0
diferencia_y = 0
hipotenusa = 0
musica = sounds.load("ronald.mp3")
musica.play(-1)
musica.set_volume(0.1)
bala_1_sfx = sounds.load("disparo.wav")
bala_1_sfx.set_volume(0.1)
bala_2_sfx = sounds.load("finger_snap.wav")
bala_2_sfx.set_volume(0.3)
bala_2_extra_sfx = sounds.load("bubble.wav")
bala_2_extra_sfx.set_volume(0.3)
big_b_sfx = sounds.load("pop.wav")
big_b_sfx.set_volume(0.3)
spin_sfx = sounds.load("rope_spin.wav")
spin_sfx.set_volume(0.4)
bala_3_sfx = sounds.load("radiator.wav")
bala_3_sfx.set_volume(0.3)
dispersion_sfx = sounds.load("plasma.wav")
bala_3_sfx.set_volume(0.7)
misil_carga = sounds.load("charge.wav")
misil_carga.set_volume(0.8)
misil_lanzamiento = sounds.load("launching.wav")
misil_lanzamiento.set_volume(0.7)
misil_explosion = sounds.load("explosion.wav")
misil_explosion.set_volume(0.6)
advertencia_bomba = sounds.load("nuclear_alert.mp3")
advertencia_bomba.set_volume(0.8)
explosion_bomba_sfx = sounds.load("explosion_bomba.wav")
giro_cooldown_sfx = 0
contador_movimiento = 0
temporizador_movimiento = 0
dif_x = 0
dif_y = 0
x = 0
y = 0
validacion_1 = False
validacion_2 = False
poder_bala = 1
contador_cambio_bala = 0
gracia_numero = 0
puntuacion = 0
pausa = False
escape_cooldown = False
constante_pausa = 23
rebote_pausa = 0
carga_1 = Actor("poder_1",(430, 170))
carga_2 = Actor("poder_2", (465, 170))
carga_3 = Actor("poder_3",(500, 170))
velocidad_balas = 0
dispersion = []
dispersados = []
misiles = []
ultima_vez = 0
reloj = pygame.time.Clock()


def draw():
    rango_visible.draw()
    for cosa in bala_circular:
        cosa[0].draw()

    for cosa in circulos_wa:
        cosa[0].draw()

    if bomba_print:
        if build == 1:
            bomba_1.draw()
        if build == 2:
            for burbuja in bomba_2:
                burbuja[0].draw()
        if build == 3:
            bomba_3.draw()
            
    if focus == True:
        gracia.draw()
        jugador.draw()
        hitbox.draw()
    else:
        jugador.draw()  
    for enemigo in enemigos:
        enemigo[0].draw()

    atacante.draw()

    for bala in balas:
        bala.draw()
    for tele in teledirigidas:
        tele.draw()
    for tele_b in teledirigido_ex:
        tele_b.draw()
    for mini in dispersados:
        mini[0].draw()
    for misi in misiles:
        misi[0].draw()


    menu_pausa.draw()

    screen.blit(fondito, (0, 0))

    for vida in numero_vidas:
        vida.draw()
    for bomba in numero_bombas:
        bomba.draw()
    screen.draw.text(str(gracia_numero), (420, 120), color="black", fontname="jaini_regular.ttf", fontsize = 30)
    screen.draw.text(str(puntuacion), (550, 60), color="black", fontname="jaini_regular.ttf", fontsize = 50)
    screen.draw.rect(vida_verde, (0, 255, 0))
    screen.draw.filled_rect(vida_verde, (0, 255, 0))
    if poder_bala >= 1:
        carga_1.draw()
    if poder_bala >= 2:
        carga_2.draw()
    if poder_bala == 3:
        carga_3.draw()
    reloj.tick()
    screen.draw.text(str(round(reloj.get_fps(), 1)), fontsize=50, fontname="jaini_regular.ttf", color="white", topright=(WIDTH-50, HEIGHT-60))


def update():
    global numero_bombas, vel_build, shift_build, ultima_vez, build, fps, balas, espera, velocidad_balas, espera_extra, constante_pausa, rebote_pausa, escape_cooldown, vida_max, lista_graciados, gracia_numero, vida_verde, daño, daño_golpe, poder_bala, puntuacion, espera_nojoda, activa, suma_1, suma_2, bomba_cd, bomba_y_vida, bomba, numero_de_bombas, invencibilidad, primera_vez, pausa, focus, bomba_print, angulo_aumento, primera_vez_rotacion, posicion_x, posicion_y, diferencia_x, diferencia_y, hipotenusa, giro_cooldown_sfx, primera_bomba, segundo, aumento_nuclear, bomba_activada, contador_explosion, numero_pa_eliminar_vida, espera_bala

    gracia.pos = jugador.pos
    if build != nueva_build:
        build = nueva_build

    direccion = ""
    if (keyboard.up):
        direccion = 'up'
        mover_jugador(direccion, vel_build, shift_build)
    if (keyboard.down):
        direccion = 'down'
        mover_jugador(direccion, vel_build, shift_build)
    if (keyboard.left) :
        direccion = 'left'
        mover_jugador(direccion, vel_build, shift_build)
    if (keyboard.right) :
        direccion = 'right'
        mover_jugador(direccion, vel_build, shift_build)
    if keyboard.q:
        spawn_enemigos(True)

    if (keyboard.z):
        disparo(True)
        cambio_bala(True)
    else:
        cambio_bala(False)

    if (keyboard.e):
        bala_circulos("si")
    else:
        bala_circulos("no")
    if not pausa:
        if (keyboard.lshift):
            focus = True
        else:
            focus = False
        
    if rotation == True:
        bomba_print = True
        if not pausa:
            numero = 0
            if primera_vez_rotacion == 0:
                posicion_x = jugador.x
                posicion_y = jugador.y
                bomba_1.pos = jugador.pos
                diferencia_x = 205 - posicion_x
                diferencia_y = 300 - posicion_y
                hipotenusa = math.sqrt((diferencia_x**2)+ (diferencia_y**2))
                primera_vez_rotacion = 1

            if bomba_1.x < 205:
                bomba_1.x += 1.2 * (abs(diferencia_x) / hipotenusa)
            else: 
                bomba_1.x -= 1.2 * (abs(diferencia_x) / hipotenusa)
            
            if bomba_1.y > 300:
                bomba_1.y -= 1.2 * (abs(diferencia_y) / hipotenusa)
            else: 
                bomba_1.y += 1.2 * (abs(diferencia_y) / hipotenusa)
            for _ in range(720):
                numero += 1
                if numero == 100:
                    if angulo_aumento < 15:
                        angulo_aumento += 0.1
                    bomba_1.angle += angulo_aumento
                    giro_cooldown_sfx += 1
                    if giro_cooldown_sfx > 135/angulo_aumento:
                        giro_cooldown_sfx = 0
                        spin_sfx.play()
    
    else:
        angulo_aumento = 0
        bomba_1.angle = 0
        bomba_1.x = 5000
        bomba_print = False
        primera_vez_rotacion = 0
        giro_cooldown_sfx = 0
        
    if bubble == True:
        bomba_print = True
        if not pausa:
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
    
    if nuclear == True:
        bomba_print = True
        if not pausa:
            if bomba_activada == False:
                if primera_bomba == 0:
                    advertencia_bomba.play()
                    bomba_3.angle = 0
                    bomba_3.x = jugador.x+5
                    bomba_3.y = jugador.y
                    primera_bomba = 1
                    aumento_nuclear = 5
                if segundo != 30:
                    segundo += 1
                else:
                    segundo = 0
                    aumento_nuclear -= 1

                bomba_3.y -= aumento_nuclear

                if aumento_nuclear < 0:
                    if bomba_3.angle != 180:
                        bomba_3.angle += 3

                if (bomba_3.y >= 574):
                    bomba_explosion(True)
                    bomba.pos = (1000, 1)
                    bomba_print = False
    else:
        primera_bomba = 0
        numero = 0
        bomba.pos = (1000, 1)
        bomba_activada = False
        contador_explosion = 0

    for burbuja in bomba_2:
        if not pausa:
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
        if not pausa:
            if not len(numero_bombas) == 0:
                if not bomba_cd:
                    activa = True
                    bomba_menos()

    if keyboard.escape:
        if not escape_cooldown:
            pausa = not pausa
            escape_cooldown = True
    else:
        escape_cooldown = False
        
    if activa == True:
        if not pausa:
            espera_nojoda += 1
            if build == 1:
                espera = 300
            if build == 2:
                espera = 600
            if build == 3:
                espera = 600

            if espera_nojoda <= espera:
                bomba_cd = True
                bomba(True)
            else:
                bomba_cd = False
                activa = False 
                espera_nojoda = 0
                bomba(False)

    if build == 1:
        if not pausa:
            if not bomba_y_vida:
                numero_de_bombas = 2
                espera_bala = 7
                velocidad_balas = 10
                vel_build = 4
                shift_build = 2
                for x in range(0, 31, 30):
                    vida = Actor("vida_sprite.png", (420+x, 50))
                    numero_vidas.append(vida)
                for x_2 in range(0, 26, 25):
                    bomba_appendar = Actor("bomba_sprite.png", (420+x_2, 90))
                    numero_bombas.append(bomba_appendar)
                    bomba_y_vida = True

    elif build == 2:
        if not pausa:
            if not bomba_y_vida:
                numero_de_bombas = 4
                espera_bala = 8
                espera_extra = 32
                velocidad_balas = 15
                vel_build = 5
                shift_build = 3
                for x in range(0, 61, 30):
                    vida = Actor("vida_sprite.png", (420+x, 50))
                    numero_vidas.append(vida)
                for x_2 in range(0, 76, 25):
                    bomba_appendar = Actor("bomba_sprite.png", (420+x_2, 90))
                    numero_bombas.append(bomba_appendar)
                    bomba_y_vida = True

    elif build == 3:
        if not pausa:
            if not bomba_y_vida:
                numero_de_bombas = 1
                espera_bala = 15
                velocidad_balas = 5
                poder_bala = 0
                vel_build = 3
                shift_build = 5 
                for x in range(0, 181, 30):
                    vida = Actor("vida_sprite.png", (420+x, 50))
                    numero_vidas.append(vida)
                for x_2 in range(0, 21, 25):
                    bomba_appendar = Actor("bomba_sprite.png", (420+x_2, 90))
                    numero_bombas.append(bomba_appendar)
                    bomba_y_vida = True

    for coso in bala_circular or circulos_wa:

        if invencibilidad == False:
            if coso[0].colliderect(hitbox):
                if not len(numero_vidas) == 0:
                    invencibilidad = True
                else:
                    sys.exit()
                
    if invencibilidad == True:
        if not pausa:
            numero_pa_eliminar_vida += 1
            if numero_pa_eliminar_vida == 1:
                numero_vidas.pop(-1)
                reinicio_bombas()
            if numero_pa_eliminar_vida == 120:
                invencibilidad = False
                numero_pa_eliminar_vida = 0

    for bala in balas:
        if not pausa:
            bala.y -= velocidad_balas
            verificar_rango(bala)
            if bala.colliderect(atacante):
                if build == 1:
                    daño += poder_bala/3
                elif build == 2:
                    daño += 0.6
                elif build == 3:
                    daño += 2
                balas.remove(bala)
                puntuacion += 20
            if build == 3:
                bala.angle += 3
                if not any(tupla[0] == bala for tupla in dispersion):
                    tupla = [bala, 0]
                    dispersion.append(tupla)

    for tupla in dispersion:
        if not pausa: 
            tupla[1] += 1
            cordi = tupla[0].pos
            if tupla[0].colliderect(atacante):
                dispersion.remove(tupla)
            if tupla[1] >= 70:
                if tupla[0] in balas:
                    balas.remove(tupla[0])
                    balas_dispersadas(cordi)
                    dispersion_sfx.play()
                if tupla in dispersion:
                    dispersion.remove(tupla)

    for tele in teledirigidas:
        if not pausa:
            teledirigir_balas(tele, 6)
            if tele.colliderect(atacante):
                daño += 0.4
                teledirigidas.remove(tele)
                puntuacion += 10
    
    for misi in misiles:
        teledirigir_balas(misi[0], 12)
        if misi[0].colliderect(atacante):
            if misi[1] == 1:
                daño += 5
            elif misi[1] == 2:
                daño += 10
            elif misi[1] == 3:
                daño += 20
            puntuacion += 100
            misil_explosion.play()
            misiles.remove(misi)

    
    if daño >= daño_golpe:
        if daño > daño_golpe:
            daño = daño - daño_golpe
        else:
            daño = 0
        vida_max -= 10
        vida_verde = Rect((65, 20), (vida_max, 10))

    for big_b in teledirigido_ex:
        if not pausa:
            teledirigir_balas(big_b, 7)
            if big_b.colliderect(atacante):
                daño += 1.5
                teledirigido_ex.remove(big_b)
                puntuacion += 20
    if vida_max > 160:
        bala_spin(True)
        movimiento_avanzado(True)
    if 70 < vida_max <=160:
        bala_circulos("si")
        bala_spin(True)
        movimiento_avanzado(True)

    if vida_max <= 70:
        daño_golpe_cambio(25)
        movimiento_avanzado(True)

    for mini in dispersados:
        if not pausa:
            mini[0].x += 6 * mini[1][0]
            mini[0].y -= 6 * mini[1][1]
            if mini[0].colliderect(atacante):
                daño += 0.3
                puntuacion += 5
                dispersados.remove(mini)
            if not mini[0].colliderect(rango_visible):
                dispersados.remove(mini)

    for cosa in bala_circular:
        if not pausa:
            cosa[0].y += 5 * cosa[1][1]
            cosa[0].x += 5 * cosa[1][0]

    for cosa in circulos_wa:
        if not pausa:
            cosa[0].y += 5 * cosa[1][1]
            cosa[0].x += 5 * cosa[1][0]

    for enemigo in enemigos:     
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
        if coso[0].colliderect(bomba_1):
            if coso in bala_circular:
                bala_circular.remove(coso)
                puntuacion += 30
        for burbuja in bomba_2:
            if coso[0].colliderect(burbuja[0]):
                if coso in bala_circular:
                    bala_circular.remove(coso)
                    puntuacion += 30    

    for coso in circulos_wa:   
        if not coso[0].colliderect(rango_visible):
            circulos_wa.remove(coso)
        if coso[0].colliderect(bomba_1):
            if coso in circulos_wa:
                circulos_wa.remove(coso)
                puntuacion += 30    
        for burbuja in bomba_2:
            if coso[0].colliderect(burbuja[0]):
                if coso in circulos_wa:
                    circulos_wa.remove(coso)
                    puntuacion += 30
    
    for bala in circulos_wa or bala_circular:
        if bala[0].colliderect(gracia):
            if not bala[0] in lista_graciados:
                lista_graciados.append(bala[0])
                gracia_numero += 1

    if pausa:
        if  rebote_pausa < 3:
            menu_pausa.x += constante_pausa
            if rebote_pausa > 0:
                constante_pausa += rebote_pausa*0.5
            if menu_pausa.x >= 203:
                rebote_pausa += 1
                constante_pausa = -constante_pausa/2
    else:
        menu_pausa.x = -163
        constante_pausa = 23
        rebote_pausa = 0

    if pausa:
        pygame.mixer.pause()
    else:
        pygame.mixer.unpause()

def mover_jugador(direccion, distancia, shift):
    if not pausa:
        if (keyboard.lshift):
            distancia = shift
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
    global contador, contador_extra, poder_bala, puntuacion, espera_bala, espera_extra
    if build == 1:
        if not pausa:
            if focus == False:
                if disparo == True:
                    contador += 1
                    if contador == espera_bala:
                        contador = 0
                        bala = Actor("bala_"+str(poder_bala), (jugador.x, jugador.y - 9))
                        balas.append(bala)
                        puntuacion += 5
                        bala_1_sfx.play()
            else:
                if disparo == True:
                    contador += 1
                    if contador == espera_bala:
                        contador = 0
                        bala = Actor('bala_'+str(poder_bala), (jugador.x, jugador.y - 9))
                        bala_2 = Actor('bala_'+str(poder_bala), (jugador.x + 15, jugador.y - 9))
                        bala_3 = Actor("bala_"+str(poder_bala), (jugador.x - 15, jugador.y - 9))
                        balas.append(bala)
                        balas.append(bala_2)
                        balas.append(bala_3)
                        puntuacion += 15
                        bala_1_sfx.play()
    elif build == 2:
        if not pausa:
            if focus == False:
                if disparo == True:
                    contador += 1
                    contador_extra += 1
                    if contador == espera_bala:
                        contador = 0
                        bala = Actor('gota', (jugador.x, jugador.y -9))
                        balas.append(bala)
                        puntuacion += 10
                        bala_2_sfx.play(1)
                    if contador_extra >= espera_extra/poder_bala:
                        contador_extra = 0
                        bala_2_extra_sfx.play()
                        puntuacion += 5
                        teledirigido = Actor('auto_bubble',(jugador.x + 15, jugador.y - 9))
                        teledirigido_2 = Actor('auto_bubble',(jugador.x - 15, jugador.y - 9))
                        teledirigidas.append(teledirigido)
                        teledirigidas.append(teledirigido_2)
            else:
                contador_extra += 1
                if contador_extra >= espera_extra-(poder_bala**2 + 2*poder_bala - 3):
                    contador_extra = 0
                    big_b_sfx.play()
                    big_b = Actor('big_b', (jugador.x , jugador.y))
                    teledirigido_ex.append(big_b)
                    puntuacion += 20
    elif build == 3:
        if not pausa:
            if focus == False:
                if disparo == True:
                    contador += 1
                    if contador == espera_bala:
                        contador = 0
                        atomo = Actor('atom', (jugador.x, jugador.y -9))
                        balas.append(atomo)
                        puntuacion += 15
                        bala_3_sfx.play()


                
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
        if objeto in dispersados:
            dispersados.remove(objeto)

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
    if not pausa:
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
    if not pausa:
        if e == "si":
            contador_enemigo_3 += 1
            if contador_enemigo_3 == 10:
                contador_enemigo_3 = 0
                for a in range(18):
                    numero_2 += 20
                    y = math.sin(math.radians(numero_2))
                    x = math.cos(math.radians(numero_2))
                    coord = (x, y)
                    bala = Actor("bala.png", atacante.pos)
                    todo = (bala, coord)
                    circulos_wa.append(todo)

def bomba(a):
    global rotation, bubble, nuclear
    if not pausa:
        if build == 1:
            if a == True:
                if not len(numero_bombas) < 0:
                    rotation = True
            else:
                rotation = False
        elif build == 2:
            if a == True:
                bubble = True
            else:
                bubble = False
        elif build == 3:
            if a == True:
                nuclear = True
            else:
                nuclear = False

def daño_golpe_cambio(entero: int):
    global daño_golpe
    daño_golpe = entero

def bomba_explosion(Comprobante):
    if not pausa:
        global activa, bomba_activada, contador_explosion, puntuacion, daño
        if Comprobante == True:
            for bala in bala_circular:
                bala_circular.remove(bala)
                puntuacion += 30
            for bala in circulos_wa:
                circulos_wa.remove(bala)
                puntuacion += 30
            if contador_explosion == 0:
                explosion_bomba_sfx.play()
            contador_explosion += 1
            daño += 4/3
            if contador_explosion == 60:
                bomba_activada = True
                if not len(numero_vidas) == 0:
                    numero_vidas.pop(-1)
                    reinicio_bombas()
                else:
                    sys.exit()
        
def bomba_menos():
    global numero_bombas
    global numero_pa_eliminar_bomba
    if not len(numero_bombas) == 0:
            if numero_pa_eliminar_bomba == 0:
                numero_pa_eliminar_bomba = 1
                numero_bombas.pop(-1)
                numero_pa_eliminar_bomba = 0

def reinicio_bombas():
    global numero_bombas
    global numero_de_bombas
    numero_bombas.clear()
    for eee in range(numero_de_bombas):
        bomba_appendar = Actor("bomba_sprite.png", (420+eee*25, 90))
        numero_bombas.append(bomba_appendar)

def movimiento_avanzado(Tru):
    global contador_movimiento, validacion_1 ,validacion_2, temporizador_movimiento, dif_x, dif_y, x, y
    if not pausa:
        if Tru == True:
            if validacion_1 and validacion_2:
                    temporizador_movimiento = 0
                    contador_movimiento = 0
                    dif_x = 0
                    dif_y = 0
                    x = 0
                    y = 0
                    validacion_1 = False
                    validacion_2 = False
            if contador_movimiento == 0:
                contador_movimiento = randint(150, 300)
            
            if not temporizador_movimiento == contador_movimiento:
                temporizador_movimiento += 1
                x = randint(42, 360)
                y = randint(34,160)
                dif_x = x - atacante.x
                dif_y = y - atacante.y

            else:
                if dif_x < 0:
                    if not atacante.x <= x:
                        atacante.x += 0.02*dif_x
                    else:
                        validacion_1 = True    
                if dif_x > 0:
                    if not atacante.x >= x:
                        atacante.x += 0.02*dif_x
                    else:
                        validacion_1 = True
                if dif_y < 0:
                    if not atacante.y <= y:
                        atacante.y += 0.02*dif_y
                    else:
                        validacion_2 = True
                if dif_y > 0:
                    if not atacante.y >= y:
                        atacante.y += 0.02*dif_y
                    else:
                        validacion_2 = True
    
def cambio_bala(sdas):
    global poder_bala, contador_cambio_bala, contador_extra, puntuacion
    if build == 1:
        if not pausa:
            if sdas:
                contador_cambio_bala += 1
                if 0<= contador_cambio_bala<= 240:
                    poder_bala = 1
                elif 240 < contador_cambio_bala <= 900:
                    poder_bala = 2
                elif 480 <contador_cambio_bala:
                    poder_bala = 3
            else:
                poder_bala = 1
                contador_cambio_bala = 0
    elif build == 2:
        if not pausa:
            if sdas:
                contador_cambio_bala += 1
                if 0<= contador_cambio_bala<= 300:
                    poder_bala = 1
                elif 300 < contador_cambio_bala <= 600:
                    poder_bala = 2
                elif 600 <contador_cambio_bala:
                    poder_bala = 3
            else:
                poder_bala = 1
                contador_cambio_bala = 0
    elif build == 3:
        if not pausa:
            if focus:
                if sdas:
                    contador_cambio_bala += 1
                    if contador_cambio_bala == 60 or contador_cambio_bala == 180 or contador_cambio_bala == 300:
                        misil_carga.play()
                    if 60 <= contador_cambio_bala<= 180:
                        poder_bala = 1
                    elif 180 < contador_cambio_bala <= 300:
                        poder_bala = 2
                    elif 300 <contador_cambio_bala:
                        poder_bala = 3
                else:
                    if poder_bala > 0:
                        misil(poder_bala)
                    puntuacion += 20*poder_bala
                    poder_bala = 0
                    contador_cambio_bala = 0

def teledirigir_balas(bala, num):
    if not pausa:
        global tele_x, tele_y, hipo, mov_x, mov_y
        tele_x = atacante.x - bala.x
        tele_y = atacante.y - bala.y
        hipo = math.sqrt(tele_x ** 2 + tele_y ** 2)

        if hipo != 0:
            mov_x = tele_x * num / hipo
            mov_y = tele_y * num / hipo
        
        bala.x +=  mov_x
        bala.y +=  mov_y
        if build == 3:
            angulo = math.degrees(math.atan2(-tele_y, tele_x))
            if mov_x != 0:
                bala.angle = angulo-90
            elif tele_x == 0 and tele_y < 0:
                bala.angle = 0
            else:
                bala.angle = 180

def balas_dispersadas(cordi):
    if not pausa:
        for angulo in range(70, 111, 10):
            if angulo == 70 or angulo == 110:
                atomo = Actor('proton', cordi)
            elif angulo == 80 or angulo == 100:
                atomo = Actor('neutron.png', cordi)
            elif angulo == 90:
                atomo = Actor('electron', cordi)
            dispersion_x = math.cos(math.radians(angulo))
            dispersion_y = math.sin(math.radians(angulo))
            cord = (dispersion_x, dispersion_y)
            tup = (atomo, cord)
            dispersados.append(tup)

def misil(poder):
    misilazo = Actor('misil', (jugador.x, jugador.y-9))
    duo = (misilazo, poder)
    misil_lanzamiento.play()
    misiles.append(duo)    

pgzrun.go()