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
    mensaje.destroy()

boton_estilo = {
    "font": ("Times News Roman", 12),  
    "fg": "white",    
    "relief": "raised",
}

boton1 = tk.Button(mensaje, text="BUILD 1", command=lambda: crear_build("1"), **boton_estilo, bg="#FF0000", activebackground="#550000", activeforeground="White")
boton2 = tk.Button(mensaje, text="BUILD 2", command=lambda: crear_build("2"), **boton_estilo, bg="#00A2E8", activebackground="#005D85", activeforeground="White")
boton3 = tk.Button(mensaje, text="BUILD 3", command=lambda: crear_build("3"), **boton_estilo, bg="#22B14C", activebackground="#125C27", activeforeground="White")

boton1.grid(row=1, column=1, padx=10, pady=5)
boton2.grid(row=2, column=0, padx=10, pady=5)
boton3.grid(row=3, column=1, padx=10, pady=5)

mensaje.mainloop()

os.environ['SDL_VIDEO_WINDOW_POS'] = '460,140'
import pygame
import pgzrun
from pgzhelper import *
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
vida_max = 320 #320
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
burbuja_sfx = sounds.load("bubble.wav")
burbuja_sfx.set_volume(0.3)
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
ran_ran_ru_sfx = sounds.load("ran_ran_ru.mp3")
ran_ran_ru_sfx.set_volume(0.7)
lluvia_sfx = sounds.load("rain.mp3")
lluvia_sfx.set_volume(1)
vine_sfx = sounds.load('vine_boom.mp3')
vine_sfx.set_volume(0.8)
fire_knife_sfx = sounds.load("fireball.wav")
fire_knife_sfx.set_volume(0.8)
poder_sfx = sounds.load("power.wav")
poder_sfx.set_volume(0.1)
lanzamiento = sounds.load("launch.wav")
lanzamiento.set_volume(0.8)
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
contador_ranranru = 0
reloj = pygame.time.Clock()
ran_ran_ru_inicio = []
nat = 3
ran_bala = []
ran_balas_grupo_1 = []
ran_balas_grupo_2 = []
ron_bala = []
ald_bala = []
ron_contador = 0
ald_contador = 0
todas_las_balas_enemigas = [bala_circular, circulos_wa, ran_bala, ron_bala, ald_bala, ran_ran_ru_inicio]
rain = False
contador_lluvia = 0
lluvia = []
bombardeo = False
contador_bombardeo = 0
misil_bombardeo = []
super_knifes = False
cuchillos = []
knife_contador = 0

def draw():
    rango_visible.draw()
    for cosa in bala_circular:
        cosa[0].draw()

    for cosa in circulos_wa:
        cosa[0].draw()

    for ran in ran_ran_ru_inicio:
        ran[0].draw()
    for ran in ran_bala:
        if ran[0].colliderect(rango_visible):
            ran[0].draw()  
    for ro in ron_bala:
        ro[0].draw()
    for al in ald_bala:
        al[0].draw()

    if bomba_print:
        if build == 1:
            bomba_1.draw()
        if build == 2:
            for burbuja in bomba_2:
                burbuja[0].draw()
        if build == 3:
            bomba_3.draw()
    for cuchillo in cuchillos:
        cuchillo.draw()
    for gota in lluvia:
        gota[0].draw()
    for misil in misil_bombardeo:
        misil[0].draw()
        
    if focus:
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
    reloj.tick(60)
    screen.draw.text(str(round(reloj.get_fps(), 1)), fontsize=50, fontname="jaini_regular.ttf", color="white", topright=(WIDTH-50, HEIGHT-60))
    screen.draw.text((f"x {jugador.x}  y {jugador.y}"), fontsize=50, fontname="jaini_regular.ttf", color="white", topright=(WIDTH-50, HEIGHT-100))

def update():
    global numero_bombas, knife_contador, contador_lluvia, contador_bombardeo, vel_build, shift_build, ultima_vez, build, fps, balas, espera, velocidad_balas, espera_extra, constante_pausa, rebote_pausa, escape_cooldown, vida_max, lista_graciados, gracia_numero, vida_verde, daño, daño_golpe, poder_bala, puntuacion, espera_nojoda, activa, suma_1, suma_2, bomba_cd, bomba_y_vida, bomba, numero_de_bombas, invencibilidad, primera_vez, pausa, focus, bomba_print, angulo_aumento, primera_vez_rotacion, posicion_x, posicion_y, diferencia_x, diferencia_y, hipotenusa, giro_cooldown_sfx, primera_bomba, segundo, aumento_nuclear, bomba_activada, contador_explosion, numero_pa_eliminar_vida, espera_bala

    gracia.pos = jugador.pos
    if build != nueva_build:
        build = nueva_build
    if keyboard.p:
        toggle_fullscreen()
        pausa = True

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
        disparo()
        cambio_bala(True)
    else:
        cambio_bala(False)

    if (keyboard.e):
        bala_circulos()

    if not pausa:
        if (keyboard.lshift):
            focus = True
        else:
            focus = False
        
    if rotation:
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
    
    if super_knifes:
        if not pausa:
            focus = True
            if knife_contador == 0 or knife_contador % 10 == 0:
                fire_knife_sfx.stop()
                for multi in range(1,6):
                    x = (multi-3)*20 + jugador.x
                    cuchillo = Actor('knife_0', (x , jugador.y-5))
                    cuchillo.images = ["knife_0", "knife_1", "knife_2", "knife_3"]
                    cuchillo.fps = 6
                    cuchillos.append(cuchillo)
                fire_knife_sfx.play()
            knife_contador += 1
    else:
        knife_contador = 0

    for cuchillo in cuchillos:
        if not pausa:
            cuchillo.animate()
            cuchillo.y -= 10
            if cuchillo.y < 10:
                cuchillos.remove(cuchillo)
            if cuchillo.colliderect(atacante):
                cuchillos.remove(cuchillo)
                daño += 0.75
    if bubble:
        bomba_print = True
        if not pausa:
            if primera_vez == 0:
                bomba_print = True
                coord = jugador.pos
                burbuja_1 = Actor("explosive_mix.png", coord)
                burbuja_1.scale = 0
                burbuja_2 = Actor("explosive_mix.png", coord)
                burbuja_2.scale = 0
                b1 = [burbuja_1, 0, 0]
                b2 = [burbuja_2, 180, 0]
                bomba_2.append(b1)
                bomba_2.append(b2)
                primera_vez = 1
    else: 
        bomba_2.clear()
        primera_vez = 0

    if rain:
        focus = True
        if not pausa:
            if contador_lluvia == 0:
                lluvia_sfx.play()
            contador_lluvia += 1
            if contador_lluvia % 2 == 0:
                y = math.sin(math.radians(260))
                x = math.cos(math.radians(260))
                gota = Actor('gota_grande', (randint(31, 429) ,14))
                mov = (x, y)
                duo = (gota, mov)
                lluvia.append(duo)
    else:
        contador_lluvia = 0

    for burbuja in bomba_2:
        if not pausa:
            if burbuja[1] == 0:
                burbuja_sfx.play()
            if (bomba_2[0][0].colliderect(atacante) and bomba_2[1][0].colliderect(atacante)) and (bomba_2[0][1] > 1800 and bomba_2[1][1] > 1800) :
                daño += math.ceil(25+(bomba_2[0][2]+bomba_2[1][2])/10)
                bomba_2.clear()
            burbuja[1] += 8
            if burbuja[0].scale < 1:
                burbuja[0].scale += 0.01
            if not burbuja[1] > 1800:
                burbuja[0].y = jugador.y - 50*math.sin(math.radians(burbuja[1])) * burbuja[0].scale
                burbuja[0].x = jugador.x + 50*math.cos(math.radians(burbuja[1])) * burbuja[0].scale

            elif burbuja[1] == 1820 or burbuja[1] == 1864:
                lanzamiento.stop()
                lanzamiento.play()
            else:
                teledirigir_balas(burbuja[0], 10)

    for gota in lluvia:
        if not pausa:
            gota[0].angle = 260
            gota[0].x += 33 * gota[1][0]
            gota[0].y -= 33 * gota[1][1]
            if gota[0].x < 28:
                lluvia.remove(gota)
            if gota[0].x > 584:
                lluvia.remove(gota)
            if gota[0].colliderect(atacante):
                daño += 0.5

    if nuclear:
        bomba_print = True
        if not pausa:
            if not bomba_activada:
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
                    bomba_explosion()
                    bomba.pos = (1000, 1)
                    bomba_print = False
    else:
        primera_bomba = 0
        numero = 0
        bomba.pos = (1000, 1)
        bomba_activada = False
        contador_explosion = 0

    if bombardeo:
        focus = True
        if not pausa:
            contador_bombardeo += 1
            if contador_bombardeo % 10 == 0:
                if contador_bombardeo in (10, 30, 50):
                    dire = 1
                else:
                    dire = 2
                vine_sfx.stop()
                if dire == 1:
                    angulo = randint(140, 220)
                    y = math.sin(math.radians(angulo))
                    x = math.cos(math.radians(angulo))
                    misil_bomba = Actor('misil', jugador.pos)
                    mov = (x, y)
                    duo = [misil_bomba, mov, 0, angulo]
                    misil_bombardeo.append(duo)
                else:
                    angulo = randint(140, 220) + 180
                    y = math.sin(math.radians(angulo))
                    x = math.cos(math.radians(angulo))
                    misil_bomba = Actor('misil', jugador.pos)
                    mov = (x, y)
                    duo = [misil_bomba, mov, 0, angulo]
                    misil_bombardeo.append(duo)
                vine_sfx.play()
    else:
        contador_bombardeo = 0

    for misil in misil_bombardeo:
        if not pausa:
            if misil[2] < 31:
                misil[2] += 1
            misil[0].angle = misil[3] - 90
            if 1 <= misil[2] < 30:
                misil[0].x += 3 * misil[1][0]/(misil[2]/6)
                misil[0].y -= 3 * misil[1][1]/(misil[2]/6)
            if misil[2] > 30:
                teledirigir_balas(misil[0], 7)

            if misil[0].colliderect(atacante):
                misil_bombardeo.remove(misil)
                daño += 40/6
                misil_explosion.play()
                puntuacion += 10

    if keyboard.a:
        bala_spin()
    
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
        
    if activa:
        if not pausa:
            espera_nojoda += 1
            if build == 1:
                espera = 300
            if build == 2:
                espera = 300   
            if build == 3:
                if focus and not bomba_cd:
                    espera = 60
                elif not focus and not bomba_cd:
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
                numero_de_bombas = 3
                espera_bala = 8
                espera_extra = 32
                velocidad_balas = 15
                vel_build = 5
                shift_build = 3
                for x in range(0, 61, 30):
                    vida = Actor("vida_sprite.png", (420+x, 50))
                    numero_vidas.append(vida)
                for x_2 in range(0, 51, 25):
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

    for listas in todas_las_balas_enemigas:
        for coso in listas:
            if invencibilidad == False:
                if not bombardeo or lluvia:
                    if coso[0].colliderect(hitbox):
                        if not len(numero_vidas) == 0:
                            invencibilidad = True
                        else:
                            sys.exit()  
            for burbuja in bomba_2:
                if burbuja[0].colliderect(coso[0]):
                    if coso in listas:
                        listas.remove(coso)
                        burbuja[2] += 1
                        if burbuja[1] < 1800:
                            poder_sfx.play()

            if bomba_1.colliderect(coso[0]):
                if coso in listas:
                    listas.remove(coso)
            for cuchillo in cuchillos:
                if cuchillo.colliderect(coso[0]):
                    if coso in listas:
                        listas.remove(coso)
            for gota in lluvia:
                if gota[0].colliderect(coso[0]):
                    if coso in listas:
                        listas.remove(coso)
                        puntuacion += 5
            for misil in misil_bombardeo:
                if misil[0].colliderect(coso[0]):
                    if coso in listas:
                        listas.remove(coso)
                
    if invencibilidad:
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
        bala_spin()
        movimiento_avanzado()
    elif 70 < vida_max <=160:
        bala_circulos()
        bala_spin()
        movimiento_avanzado()
    elif 0 < vida_max <= 70:
        daño_golpe_cambio(25)
        ran_ran_ru(180)
        ron()
        ald()
    elif vida_max == 0:
        limpiar_pantalla()
  
    for mini in dispersados:
        if not pausa:
            mini[0].x += 10 * mini[1][0]
            mini[0].y -= 10 * mini[1][1]
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

    for coso in circulos_wa:   
        if not coso[0].colliderect(rango_visible):
            circulos_wa.remove(coso)
    
    for ran in ran_ran_ru_inicio:
        if not pausa:
            global nat
            nat = 3
            if ran[1] == 1:  
                y = ran[0].y          
                ran[2] -= 0.1
                ran[0].x += ran[2]
                if ran[0].x < 20 and ran[2] < 0:
                    ran_ran_ru_inicio.remove(ran)
                    ran_exposure(20, y, ran[1])
            elif ran[1] == 2:
                y = ran[0].y          
                ran[2] -= 0.1
                ran[0].x -= ran[2]
                if ran[0].x > 389 and ran[2] < 0:
                    ran_ran_ru_inicio.remove(ran)
                    ran_exposure(389, y, ran[1])

            elif ran[1] == 3:
                x = ran[0].x
                ran[2] -= 0.1
                ran[0].y += ran[2]
                if ran[0].y < 14 and ran[2] < 0:
                    ran_ran_ru_inicio.remove(ran)
                    ran_exposure(x, 14, ran[1])
            else:
                x = ran[0].x
                ran[2] -= 0.1
                ran[0].y -= ran[2]
                if ran[0].y > 586 and ran[2] < 0:
                    ran_ran_ru_inicio.remove(ran)
                    ran_exposure(x, 586, ran[1])
                    
    for ran in ran_bala:
        if not pausa:
            for ran_2 in ran_bala:
                if ran[0].colliderect(ran_2[0]):
                    if ran != ran_2:
                        if ran[3] != 0 and ran_2[3] != 0:
                            if ran[2] in (1, 2):
                                ran[1][1] = 0
                                ran_2[1][1] = 0
                            else:
                                ran[1][0] = 0
                                ran_2[1][0] = 0
            if ran[3] == 1:
                ran_balas_grupo_1.append(ran)
            elif ran[3] == 2:
                ran_balas_grupo_2.append(ran)

            if ran[2] in (1 ,2):
                ran[0].x += ran[1][0] * 6
                ran[0].y += ran[1][1] * 3
            else:
                ran[0].x += ran[1][0] * 3
                ran[0].y += ran[1][1] * 6

            if ran[2] == 2:
                if ran[0].x < 20: 
                    if ran in ran_bala:
                        ran_bala.remove(ran)
            if ran[2] == 1:
                if ran[0].x > 389: 
                    if ran in ran_bala:
                        ran_bala.remove(ran)
            if ran[2] == 4:
                if ran[0].y < 9: 
                    if ran in ran_bala:
                        ran_bala.remove(ran)
            if ran[2] == 3:
                if ran[0].y > 591:
                    if ran in ran_bala:
                        ran_bala.remove(ran)

    for lista in todas_las_balas_enemigas:
        for bala in lista:
            if bala[0].colliderect(gracia):
                if bala not in lista_graciados:
                    lista_graciados.append(bala)
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

    for ro in ron_bala:
        if not pausa:
            ro[1] += 3
            ro[0].x = ro[2] + math.sin(math.radians(ro[1])) * 10
            ro[0].y += 2
            if ro[0]. y > 594:
                ron_bala.remove(ro)
            
    for al in ald_bala:
        if not pausa:
            al[1] += 3
            al[0].y = al[2] + math.sin(math.radians(al[1])) * 10
            al[0].x -= 2
            if al[0]. x < 11:
                ald_bala.remove(al)
            
def mover_jugador(direccion, distancia, shift):
    if not pausa:
        if focus:
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
def disparo():
    global contador, contador_extra, poder_bala, puntuacion, espera_bala, espera_extra
    if build == 1:
        if not pausa:
            if not focus:
                contador += 1
                if contador == espera_bala:
                    contador = 0
                    bala = Actor("bala_"+str(poder_bala), (jugador.x, jugador.y - 9))
                    balas.append(bala)
                    puntuacion += 5
                    bala_1_sfx.play()
            else:
                if not super_knifes:
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
            if not focus:
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
                    burbuja_sfx.play()
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
            if not focus:
                contador += 1
                if contador == espera_bala:
                    contador = 0
                    atomo = Actor('atom', (jugador.x, jugador.y -9))
                    balas.append(atomo)
                    puntuacion += 15
                    bala_3_sfx.play()


                
def spawn_enemigos(enemigo):
    global contador_enemigo
    if enemigo:
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

def bala_spin():   
    global numero
    global contador_enemigo
    if not pausa:
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

def bala_circulos():
    global numero_2
    global contador_enemigo_3
    if not pausa:
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

def bomba(comprobante):
    global rotation, super_knifes, bubble, rain, nuclear, bombardeo
    if not pausa:
        if build == 1:
            if comprobante:
                if focus and not rotation:
                    super_knifes = True
                elif not super_knifes:
                    rotation = True
            else:
                rotation = False
                super_knifes = False
        elif build == 2:
            if comprobante:
                if focus and not bubble:
                    rain = True
                elif not rain:
                    bubble = True
            else:
                bubble = False
                rain = False
        elif build == 3:
            if comprobante:
                if focus and not nuclear:
                    bombardeo = True
                elif not bombardeo:
                    nuclear = True
            else:
                bombardeo = False
                nuclear = False

def daño_golpe_cambio(entero: int):
    global daño_golpe
    daño_golpe = entero

def bomba_explosion():
    if not pausa:
        global activa, bomba_activada, contador_explosion, puntuacion, daño
        limpiar_pantalla()
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

def movimiento_avanzado():
    global contador_movimiento, validacion_1 ,validacion_2, temporizador_movimiento, dif_x, dif_y, x, y
    if not pausa:
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
    
def cambio_bala(comprobante):
    global poder_bala, contador_cambio_bala, contador_extra, puntuacion
    if build == 1:
        if not pausa:
            if comprobante:
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
            if comprobante:
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
                if comprobante:
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

def ran_ran_ru(valor):
    global contador_ranranru
    if not pausa:
        contador_ranranru += 1 
        if contador_ranranru >= valor:
            contador_ranranru = 0
            numero = randint(1, 4)
            if numero == 1:
                y = randint(67, 533)
                x = 33
            elif numero == 2:
                y = randint(67, 533)
                x = 377
            elif numero == 3:
                x = randint(73, 297)
                y = 27
            else:
                x = randint(73, 297)
                y = 573
            balas = Actor("mc_bala", (x, y))
            velo = 3
            todo = [balas, numero, velo]
            ran_ran_ru_inicio.append(todo)
                
def ran_exposure(x, y, direccion):
    if not pausa:
        if direccion == 1: #Izquierda
            ran_ran_ru_sfx.play()
            for _ in range(141):
                if _ in (5, 15, 20, 25, 35, 40):
                    balas_ran1 = Actor("mc_bala", (x-_*5, y - 6*_))
                    balas_ran2 = Actor("mc_bala", (x-_*5, y + 6*_))
                    vel = (1 , 1.1)
                    vel2 = (1 , -1.1)
                    trio_1 = (balas_ran1, vel, direccion, 0)
                    trio_2 = (balas_ran2, vel2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (50, 55, 65, 70, 80):
                    balas_ran1 = Actor("mc_bala", (x-_*5, y - 3*_))
                    balas_ran2 = Actor("mc_bala", (x-_*5, y + 3*_))
                    vel = [1 , 0.7]
                    vel2 = [1 , -0.7]
                    trio_1 = [balas_ran1, vel, direccion, 1]
                    trio_2 = [balas_ran2, vel2, direccion, 2]
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (90, 95, 105, 110, 120, 125, 135, 140):
                    balas_ran1 = Actor("mc_bala", (x-_*5, y - 40))
                    balas_ran2 = Actor("mc_bala", (x-_*5, y + 40))
                    vel = (1 , 0)
                    vel2 = (1 , 0)
                    trio_1 = (balas_ran1, vel, direccion, 0)
                    trio_2 = (balas_ran2, vel2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)

        elif direccion == 2: #Derecha
            ran_ran_ru_sfx.play()
            for _ in range(141):
                if _ in (5, 15, 20, 25, 35, 40):
                    balas_ran1 = Actor("mc_bala", (x+_*5, y - 6*_))
                    balas_ran2 = Actor("mc_bala", (x+_*5, y +6*_))
                    vel = (-1 , 1.1)
                    vel2 = (-1 , -1.1)
                    trio_1 = (balas_ran1, vel, direccion, 0)
                    trio_2 = (balas_ran2, vel2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (50, 55, 65, 70, 80):
                    balas_ran1 = Actor("mc_bala", (x+_*5, y - 3*_))
                    balas_ran2 = Actor("mc_bala", (x+_*5, y + 3*_))
                    vel = [-1 , 0.7]
                    vel2 = [-1 , -0.7]
                    trio_1 = [balas_ran1, vel, direccion, 1]
                    trio_2 = [balas_ran2, vel2, direccion, 2]
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (90, 95, 105, 110, 120, 125, 135, 140):
                    balas_ran1 = Actor("mc_bala", (x+_*5, y - 40))
                    balas_ran2 = Actor("mc_bala", (x+_*5, y + 40))
                    vel = (-1 , 0)
                    vel2 = (-1 , 0)
                    trio_1 = (balas_ran1, vel, direccion, 0)
                    trio_2 = (balas_ran2, vel2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                
        elif direccion == 3: #Abajo
            ran_ran_ru_sfx.play()
            for _ in range(141):
                if _ in (5, 15, 20, 25, 35, 40):
                    balas_ran1 = Actor("mc_bala", (x + 6 * _, y - _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 6 * _, y - _ * 5))
                    vel = (-1.1 , 1)
                    vel2 = (1.1, 1)
                    trio_1 = (balas_ran1, vel, direccion, 0)
                    trio_2 = (balas_ran2, vel2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (50, 55, 65, 70, 80):
                    balas_ran1 = Actor("mc_bala", (x + 3 * _, y - _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 3 * _, y - _ * 5))
                    vel = [-0.7 , 1]
                    vel2 = [0.7 , 1]
                    trio_1 = [balas_ran1, vel, direccion, 1]
                    trio_2 = [balas_ran2, vel2, direccion, 2]
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (90, 95, 105, 110, 120, 125, 135, 140):
                    balas_ran1 = Actor("mc_bala", (x + 40, y - _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 40, y - _ * 5))
                    vel = (0 , 1)
                    vel2 = (0 , 1)
                    trio_1 = (balas_ran1, vel, direccion, 0)
                    trio_2 = (balas_ran2, vel2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)

        else: #Arriba
            ran_ran_ru_sfx.play()
            for _ in range(141):
                if _ in (5, 15, 20, 25, 35, 40):
                    balas_ran1 = Actor("mc_bala", (x + 6 * _, y + _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 6 * _, y + _ * 5))
                    vel = (-1.1 , -1)
                    vel2 = (1.1, -1)
                    trio_1 = (balas_ran1, vel, direccion, 0)
                    trio_2 = (balas_ran2, vel2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (50, 55, 65, 70, 80):
                    balas_ran1 = Actor("mc_bala", (x + 3 * _, y + _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 3 * _, y + _ * 5))
                    vel = [-0.7 , -1]
                    vel2 = [0.7 , -1]
                    trio_1 = [balas_ran1, vel, direccion, 1]
                    trio_2 = [balas_ran2, vel2, direccion, 2]
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (90, 95, 105, 110, 120, 125, 135, 140):
                    balas_ran1 = Actor("mc_bala", (x + 40, y + _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 40, y + _ * 5))
                    vel = (0 , -1)
                    vel2 = (0 , -1)
                    trio_1 = (balas_ran1, vel, direccion, 0)
                    trio_2 = (balas_ran2, vel2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)

def ron():
    global ron_contador
    if not pausa:
        ron_contador += 1
        if ron_contador >= 60:
            ron_contador = 0
            for x in range(31, 380, 58):
                va = x
                bala_mov = Actor("bala_azul.png", (x , 7))
                dio = [bala_mov, 0, va]
                ron_bala.append(dio)

def ald():
    global ald_contador
    if not pausa:
        ald_contador += 1
        if ald_contador >= 90:
            ald_contador = 0
            for y in range(26, 576, 61):
                va = y
                bala_mov = Actor("bala_azul.png", (397 , y))
                dio = [bala_mov, 0, va]
                ald_bala.append(dio)

def limpiar_pantalla():
    if not pausa:
        for lista in todas_las_balas_enemigas:
            lista.clear()


pgzrun.go()