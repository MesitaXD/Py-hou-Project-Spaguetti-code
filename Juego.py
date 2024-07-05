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
from random import randint, choice
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
daño_golpe = 0.75
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

jugador = Actor('jugador.jpg', (244, 530))
cubo_dialogo = Actor('dialogo_cubo.png', (244, 631)) #(244, 510)
hitbox = Actor('hitbox.png', (244, 530))
gracia = Actor('graze_semi.png', (jugador.x, jugador.y))
menu_pausa = Actor('pausa.png', (-163, 300))
imagen = Actor("ronald.png", (800, 0))

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
rango_visible = Actor("cubo_visible.jpg", (244, 300))
ronald = Actor("jugador.jpg", (244, 90))
bomba_1 = Actor("no_evidence.png", (1, 1))
bala_circular = []
circulos_wa = []
aleatorio = 0
contador_enemigo_2 = 0
contador_enemigo_3 = 0
numero_2 = 0
numero_3 = 0
vida_max = 320 #320
numero_vidas = []
numero_bombas = []
vida_verde =  Rect((65, 25), (vida_max, 10))
numero_de_bombas = 0
primera_vez_rotacion = 0
posicion_x = 0
posicion_y = 0
diferencia_x = 0
diferencia_y = 0
hipotenusa = 0
# Sfx
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
spellcard = sounds.load("spellcard.wav")
spellcard.set_volume(1)
ataque_5 = sounds.load("attack5.wav")
ataque_5.set_volume(0.8)
beep = sounds.load("beep.wav")
beep.set_volume(1)
tick = sounds.load("tick.wav")
tick.set_volume(1)
muerte = sounds.load("dead.wav")
muerte.set_volume(0.2)
bonus = sounds.load("bonus.wav")
bonus.set_volume(0.8)
# mas cosas
giro_cooldown_sfx = 0
contador_movimiento = 0
contador_movimiento_circular = 0
direccion_movimiento_circular = 1
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
carga_1 = Actor("poder_1",(509, 170))
carga_2 = Actor("poder_2", (544, 170))
carga_3 = Actor("poder_3",(579 , 170))
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
rain = False
contador_lluvia = 0
lluvia = []
spell = True
bombardeo = False
contador_bombardeo = 0
misil_bombardeo = []
super_knifes = False
cuchillos = []
knife_contador = 0
fase = 8  #-70
nueva_fase = False
contador_cajitas = 0
cajitas_feliz = []
fps = 60
puntos = []
papas = []
contador_papas = 0
contador_papas_2 = 0
contador_tomate = 0
contador_tomate_2 = 0
tomate_dire = 0
tomates = []
nute = True
wasa = 0
Ripp = []
contador_rip_1 = 0
contador_rip_2 = 0
contador_rip_3 = 0
todas_las_balas_enemigas = [tomates, bala_circular, circulos_wa, ran_bala, ron_bala, ald_bala, ran_ran_ru_inicio, cajitas_feliz, papas, Ripp]
pruebas = []
contador_tiempo = 0
tiempo_limite = 30
tiempo_normal = (30, 30, 30, 30, 30, 30, 30)
tiempo_spellcards = (40, 45, 40, 35)
nombre_spellcard = ""
contador_spellcard = 0
spellcard_x = 0
spellcard_y = 0
spellcard_tamaño = 0
spellcard_transparencia = 0
spellcard_bonus_transparencia = 0
spellcard_bonus = 0
contador_bonus = -1
contador_suma = 0
bonus_visible = 0
lista_bonus = (1200000, 1800000, 2300000)
bonus_visible_2 = 0
spellcard_obtenido = ""
spellcard_fallida = False
mostrar_spellcard = False
dialogo_contador = 0
numero_dialogo = -1
dialogos = None 
dialogo = "None"
dialogo_op = 0
color_dialogo = None
lista_spellcards = ('McRoll: "Ran Ran Ru!!"', 'house special: "McNuggets buffet"', 'Fried: French With some Tomatoes', "Ripples Of 495 Menus")
def draw():
    rango_visible.draw()

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
    for punto in puntos:
        punto[0].draw()
    for enemigo in enemigos:
        enemigo[0].draw()
    for cosa in bala_circular:
        cosa[0].draw()
    for rip in Ripp:
        rip[0].draw()
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
    for cajas in cajitas_feliz:
        cajas[0].draw()
    for papa in papas:
        papa[0].draw()
    for tomate in tomates:
        tomate[0].draw()
    ronald.draw()

    for bala in balas:
        if not build == 1:
            bala.draw()
        else:
            bala[0].draw()
    for tele in teledirigidas:
        tele.draw()
    for tele_b in teledirigido_ex:
        tele_b.draw()
    for mini in dispersados:
        mini[0].draw()
    for misi in misiles:
        misi[0].draw()

    imagen.draw()
    cubo_dialogo.draw()
    screen.draw.text((f"{dialogo}"), fontsize=22, fontname="jaini_regular.ttf", color="white", topleft=(57, 458), alpha = dialogo_op, owidth=1, ocolor=color_dialogo, width=374)
    screen.draw.text((f"{nombre_spellcard}"), fontsize=spellcard_tamaño, fontname="jaini_regular.ttf", color="white", midright=(spellcard_x, spellcard_y), alpha = spellcard_transparencia, owidth=1, ocolor="black")
    screen.draw.text((f"Bonus   {spellcard_bonus}"), fontsize=22 , fontname="jaini_regular.ttf", color="white", midleft=(spellcard_x - len(nombre_spellcard)*8.75, 84), alpha = spellcard_bonus_transparencia, owidth=1, ocolor="black")
    screen.draw.text((f"{spellcard_obtenido}"), fontsize=40 , fontname="jaini_regular.ttf", color="white", center=(244, 90), alpha = bonus_visible, owidth=1, ocolor="black")
    screen.draw.text((f"+{spellcard_bonus}"), fontsize=35 , fontname="jaini_regular.ttf", color="white", center=(244, 130), alpha = bonus_visible_2, owidth=1, ocolor="black")
    menu_pausa.draw()
    screen.blit(fondito, (0, 0))

    for vida in numero_vidas:
        vida.draw()
    for bomba in numero_bombas:
        bomba.draw()

    screen.draw.text(str(gracia_numero), (499, 120), color="black", fontname="jaini_regular.ttf", fontsize = 30)
    screen.draw.text(str(puntuacion), (629, 60), color="black", fontname="jaini_regular.ttf", fontsize = 50)
    screen.draw.rect(vida_verde, (0, 255, 0))
    screen.draw.filled_rect(vida_verde, (0, 255, 0))
    if poder_bala >= 1:
        carga_1.draw()
    if poder_bala >= 2:
        carga_2.draw()
    if poder_bala == 3:
        carga_3.draw()
    for bala in pruebas:
        bala[0].draw()
    reloj.tick(fps)
    screen.draw.text(str(round(reloj.get_fps(), 1)), fontsize=50, fontname="jaini_regular.ttf", color="white", topright=(WIDTH-50, HEIGHT-60))
    screen.draw.text((f"x {jugador.x}  y {jugador.y}"), fontsize=50, fontname="jaini_regular.ttf", color="white", topright=(WIDTH-50, HEIGHT-100))
    screen.draw.text((f"{tiempo_limite}"), fontsize=40, fontname="jaini_regular.ttf", color="white", topright=(462, 4), owidth=1, ocolor="orange")
    #for lista in todas_las_balas_enemigas:
     #   for coso in lista:
      #       screen.draw.rect(coso[2].get_rect(), (255,0,0))
    screen.draw.rect(hitbox.get_rect(), (255,0,0))


def update():
    global  contador_suma, spellcard_fallida, numero_dialogo, dialogo_contador, contador_tiempo, mostrar_spellcard, numero_bombas, nute, fase, spell, tiempo_limite
    global contador_movimiento, contador_movimiento, fps, nueva_fase, knife_contador, contador_lluvia, contador_bombardeo, vel_build, shift_build, ultima_vez, build
    global fps, balas, espera, velocidad_balas, espera_extra, constante_pausa, rebote_pausa, escape_cooldown, vida_max, lista_graciados, gracia_numero, vida_verde, daño 
    global daño_golpe, poder_bala, puntuacion, espera_nojoda, activa, suma_1, suma_2, bomba_cd, bomba_y_vida, bomba, numero_de_bombas, invencibilidad, primera_vez, pausa
    global focus, bomba_print, angulo_aumento, primera_vez_rotacion, posicion_x, posicion_y, diferencia_x, diferencia_y, hipotenusa, giro_cooldown_sfx, primera_bomba
    global segundo, aumento_nuclear, bomba_activada, contador_explosion, numero_pa_eliminar_vida, espera_bala, dialogos
    

    if build != nueva_build:
        build = nueva_build
    if dialogos == None:
        if build == 1:
            dialogos = (('Hay un dicho que me encanta: "El momento donde una estrella más brilla es cuando mueren. En ese caso eso aplicará para mí algún día.', 1),
    ('O tal vez ese día no esté tan lejos de lo esperado. O mi utopía', 1), ('Donde el juez sentencia su veredicto: "Te condeno a..." No escuché ninguna palabra aparte de esas.', 1),
    ('Te preguntarás cuál fue el veredicto, yo creo que era el olvido.', 1), ('Igual que una vela, una vez se prende tiene una cuenta regresiva antes de derretirse y dejar de iluminar.', 1),
    ('Yo soy una vela, mi propósito es iluminar, sacrificándome en el proceso', 1), ('Y mi llama son nada más que mis recuerdos, mi convicción.', 1),
    ('Prepara el escenario, hoy posiblemente logre mi objetivo de ser más brillante que el sol.', 1), ('RAN RAN RU!!', 0), ('...', 1), 
    ('Como que mi convicción ha disminuido ante tal enemigo, al parecer mi día va a demorar más', 1), ('Qué hamburguesa más rara...', 0), 
    ('De todas maneras, aún deberías servir para ser lanzado, ¿quién se supone que eres?', 0))
        elif build == 2:
            dialogos =  (("Mmh, este día es extraño, primero estamos normales, luego aparece un portal hacia este lugar extraño que huele a aceite quemado", 1), 
    ("De ese portal salen un montón de cosas de comida rápida, hamburguesas, papas, nuggets, tomates...", 1), ("Estoy confundido, fui enviado a ver qué había pasado pero... No veo nada, quizá esto no tiene causante y fue una fisura?", 1), 
    ("Quiero decir, una fisura tampoco suena tan mal...", 1), ("RAN RAN RU!", 0), ("...", 1), ("¡RONALD McDONALD?!", 1), ("Ok, ahora me emocioné jeje, ¿qué se supone que hace Ronald McDonald en este lugar?", 1),
    ("La pregunta sería, ¿qué haces TÚ en la casa de Ronald, no recuerdo haberte dejado entrar...", 0), ("Ah bueno, quizá será porque no lo hiciste jeje, un portal se abrió por... Mi casa, y de ahí salen cosas que están causando estragos", 1),
    ("Ah... Espera, ¿entonces un niño entró a un portal desconocido del cual salen cosas peligrosas, solo?", 0), ("Bueno, si lo pones de tal forma... No es la primera vez que vengo a lugares así, no te confíes, payaso", 1),
    ("No tengo idea de quién seas, pero tienes agallas, niño, veamos si no abres más la boca de lo que puedes comer", 0))
        elif build == 3:
            la_lista = ((("...", 1), ("Hola! Soy un basado!", 0), ("Ohhh, ere un basado?", 1), ("Si! Un basado!", 0), ("BAS-A-DO RMIR", 1)), (("...", 1), ("Adios!!", 0), ("Ah, Adios?!", 1), ("Sii! Adios!", 0), ("Pues adios.", 1), ("... Ay no mames, funciono", 0), ("Adiosito vas a ver!!", 1)), (("...", 1), ("Hola! Soy un payaso!", 0), ("Ah enserio? Y tu conoces el tema?", 1), ("Uh? Cual tema?", 0), ("El Tema-dreo!", 1)))
            dialogos = choice(la_lista)
    if not pausa:
        if fase < 0:
            fase += 1
        if fase == -1:
            dialogo_contador = 1
    
    if keyboard.p:
        toggle_fullscreen()
        pausa = True
    if keyboard.u:
        fps = 30
    else:
        fps = 60
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
    
    if keyboard.LCTRL:
        if fase == 0:
            if dialogo_contador == 0:
                dialogo_contador = 1
            
    if (keyboard.z):
        if 1 <= fase:
            disparo()
            cambio_bala(True)
        elif fase == 0:
            if dialogo_contador == 0:
                dialogo_contador += 1
    else:
        cambio_bala(False)


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
                diferencia_x = 244 - posicion_x
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
            if cuchillo.colliderect(ronald):
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
            if (bomba_2[0][0].colliderect(ronald) and bomba_2[1][0].colliderect(ronald)) and (bomba_2[0][1] > 1800 and bomba_2[1][1] > 1800) :
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
                teledirigir_balas(burbuja[0], 10, ronald)

    for gota in lluvia:
        if not pausa:
            gota[0].angle = 260
            gota[0].x += 33 * gota[1][0]
            gota[0].y -= 33 * gota[1][1]
            if gota[0].x < 28:
                lluvia.remove(gota)
            if gota[0].x > 584:
                lluvia.remove(gota)
            if gota[0].colliderect(ronald):
                daño += 0.6

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
                    spellcard_balas()
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
                teledirigir_balas(misil[0], 7, ronald)

            if misil[0].colliderect(ronald):
                misil_bombardeo.remove(misil)
                daño += 30/6
                misil_explosion.play()
                puntuacion += 700

    if keyboard.a:
        bala_spin()
    
    if keyboard.x:
        if not pausa:
            if fase > 0:
                if not len(numero_bombas) == 0:
                    if not bomba_cd:
                        numero_pa_eliminar_vida = 0 
                        spellcard_fallida = True
                        activa = True
                        spellcard.play()
                        bomba_menos()
    if keyboard.e:
        titulo_spellcard(True)
    else:
        pass
        #titulo_spellcard(False)
        
    if keyboard.escape:
        if not escape_cooldown:
            pausa = not pausa
            escape_cooldown = True
    else:
        escape_cooldown = False
        
    if activa:
        if not pausa:
            invencibilidad = True
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
                invencibilidad = False
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
                for x in range(0, 61, 30):
                    vida = Actor("vida_sprite.png", (499+x, 50))
                    numero_vidas.append(vida)
                for x_2 in range(0, 26, 25):
                    bomba_appendar = Actor("bomba_sprite.png", (499+x_2, 90))
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
                for x in range(0, 91, 30):
                    vida = Actor("vida_sprite.png", (499+x, 50))
                    numero_vidas.append(vida)
                for x_2 in range(0, 51, 25):
                    bomba_appendar = Actor("bomba_sprite.png", (499+x_2, 90))
                    numero_bombas.append(bomba_appendar)
                    bomba_y_vida = True

    elif build == 3:
        if not pausa:
            if not bomba_y_vida:
                numero_de_bombas = 10
                espera_bala = 15
                velocidad_balas = 5
                poder_bala = 0
                vel_build = 3
                shift_build = 5 
                for x in range(0, 181, 30):
                    vida = Actor("vida_sprite.png", (499+x, 50))
                    numero_vidas.append(vida)
                for x_2 in range(0, 21, 25):
                    bomba_appendar = Actor("bomba_sprite.png", (499+x_2, 90))
                    numero_bombas.append(bomba_appendar)
                    bomba_y_vida = True

    for listas in todas_las_balas_enemigas:
        for coso in listas:
            if invencibilidad == False:
                if coso[2].obb_collideobb(hitbox):
                    if not len(numero_vidas) == 0:
                        invencibilidad = True
                        spellcard_fallida = True
                        muerte.play()
                    else:
                        sys.exit()

            for burbuja in bomba_2:
                if burbuja[0].colliderect(coso[0]):
                    if coso in listas:
                        listas.remove(coso)
                        burbuja[2] += 1
                        puntuacion += 150
                        if burbuja[1] < 1800:
                            poder_sfx.play()

            if bomba_1.obb_collideobb(coso[0]):
                if coso in listas:
                    listas.remove(coso)
                    puntuacion += 100
            for cuchillo in cuchillos:
                if cuchillo.colliderect(coso[0]):
                    if coso in listas:
                        puntuacion += 150
                        listas.remove(coso)
            for gota in lluvia:
                if gota[0].colliderect(coso[0]):
                    if coso in listas:
                        listas.remove(coso)
                        puntuacion += 100
            for misil in misil_bombardeo:
                if misil[0].colliderect(coso[0]):
                    if coso in listas:
                        listas.remove(coso)

    if invencibilidad:
        if not pausa:
            if not activa:
                numero_pa_eliminar_vida += 1
                if numero_pa_eliminar_vida == 1:
                    numero_vidas.pop(-1)
                    reinicio_bombas()
                if numero_pa_eliminar_vida == 180:
                    invencibilidad = False
                    numero_pa_eliminar_vida = 0
        

    for bala in balas:
        if not pausa:
            if not build == 1:
                bala.y -= velocidad_balas
            else:
                if bala[1] == 0:
                    if bala[2] == 1:
                        bala[0].y += velocidad_balas
                    else:
                        sen = math.sin(math.radians(260+10*bala[2]))
                        cos = math.cos(math.radians(260+10*bala[2]))
                        bala[0].y -= sen*velocidad_balas
                        bala[0].x += cos*velocidad_balas
                else:
                    bala[0].y -= velocidad_balas
            verificar_rango(bala)
            if not build == 1:
                if bala.colliderect(ronald):                        
                    if build == 2:
                        daño += 0.7
                    elif build == 3:
                        daño += 1.5
                    balas.remove(bala)
                    puntuacion += 20
            else:
                if bala[0].colliderect(ronald):
                    daño += poder_bala/5
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
            if tupla[0].colliderect(ronald):
                dispersion.remove(tupla)
            if tupla[1] >= 70:
                if tupla[0] in balas:
                    balas.remove(tupla[0])
                    balas_dispersadas(cordi)
                    dispersion_sfx.stop()
                    dispersion_sfx.play()
                if tupla in dispersion:
                    dispersion.remove(tupla)

    for tele in teledirigidas: 
        if not pausa:
            teledirigir_balas(tele, 6, ronald)
            if tele.colliderect(ronald):
                daño += 0.4
                teledirigidas.remove(tele)
                puntuacion += 10
    
    for misi in misiles:
        teledirigir_balas(misi[0], 12, ronald)
        if misi[0].colliderect(ronald):
            if misi[1] == 1:
                daño += 5
            elif misi[1] == 2:
                daño += 10
            elif misi[1] == 3:
                daño += 20
            puntuacion += 100
            misil_explosion.stop()
            misil_explosion.play()
            misiles.remove(misi)

    if not pausa:
        if daño >= daño_golpe:
            if daño > daño_golpe:
                daño = daño - daño_golpe
            else:
                daño = 0
            vida_max -= 3
            vida_verde = Rect((65, 25), (vida_max, 10)) 

    for big_b in teledirigido_ex:
        if not pausa:
            teledirigir_balas(big_b, 7, ronald)
            if big_b.colliderect(ronald):
                daño += 2
                teledirigido_ex.remove(big_b)
                puntuacion += 20
    if mostrar_spellcard:
        agregar_bonus()

    if not pausa:
        if fase < 1:
            if not numero_dialogo < len(dialogos):
                cubo_dialogo_mov(0)
            else:
                cubo_dialogo_mov(1)
        if dialogo_contador == 1:
            dialogo_contador += 1
            if keyboard.LCTRL:
                dialogo_contador = 90
            numero_dialogo += 1
            if not numero_dialogo < len(dialogos):
                clock.schedule(musica_play, 1)
                clock.schedule(fase_inicio, 0.5)
                dialogo_contador = 0
                dialogo_a_mostrar("end")
        elif 100 > dialogo_contador > 1:
            dialogo_a_mostrar(dialogos[numero_dialogo])
            # print(dialogos[numero_dialogo])
            dialogo_contador += 1
        elif dialogo_contador >= 100:
            dialogo_contador = 0
    
    if not pausa:
        if fase == 1:
            if not nueva_fase:
                if vida_max > 70:
                    tiempo_contador(1)
                    bala_spin(10)
                    rotacion_bala_personalizada(4, ronald.pos, 1, "bala", -5, 0, 6)
                    movimiento_avanzado(0, 0.02, 0, 0)
                elif 0 < vida_max <= 70:
                    titulo_spellcard(True)
                    movimiento_avanzado(1, 0.02, 244, 90)
                    if vida_max > 65:
                        spellcard_fallida = False
                        spellcard.play()
                        spellcard_balas()
                        vida_max = 64
                    if spell:
                        contador_tiempo = 60
                        spell = spellcard_ronald(spell)
                        daño = -25
                        tiempo_limite = tiempo_spellcards[fase-1]
                    if not spell:
                        tiempo_contador(0)
                        daño_golpe_cambio(4)
                        ran_ran_ru(180)
                        ron()
                        ald()
                        bonus_score(True)
                elif vida_max <= 0:
                    ran_ran_ru_sfx.stop()
                    bonus.play()
                    bonus_score(False)
                    titulo_spellcard(False)
                    tiempo_limite = tiempo_normal[fase]
                    contador_movimiento = 0
                    vida_max = 0
                    contador_suma = 0
                    nueva_fase = True
            else:
                mostrar_spellcard = True
                cambio_fase()
                spellcard_balas()
        elif fase == 2:
            if not nueva_fase:
                if vida_max > 70:
                    tiempo_contador(1)
                    bala_spin(6)
                    rotacion_bala_personalizada(6, ronald.pos, 4, "bala", -5, 0, 8)
                    movimiento_avanzado(0, 0.03, 0, 0)
                    daño_golpe_cambio(1)
                elif 0 < vida_max <= 70:
                    titulo_spellcard(True)
                    if vida_max > 65:
                        temporizador_movimiento
                        spellcard_fallida = False
                        spellcard.play()
                        spellcard_balas()
                        vida_max = 64
                    if spell:
                        movimiento_avanzado(1, 0.03, 444, 300)
                        contador_tiempo = 0
                        spell = spellcard_ronald(spell)
                        daño = -10
                        tiempo_limite = tiempo_spellcards[fase-1]
                    if not spell:
                        movimiento_circular((244, 300), 200, 270, 1, 1)
                        bonus_score(True)
                        tiempo_contador(0)
                        daño_golpe_cambio(4)
                        cajitas(150)
                elif vida_max <= 0:
                    bonus.play()
                    bonus_score(False)
                    titulo_spellcard(False)
                    tiempo_limite = tiempo_normal[fase]
                    contador_movimiento = 0
                    vida_max = 0
                    contador_suma = 0
                    nueva_fase = True
            else:
                movimiento_avanzado(1, 0.03, 244, 90)
                mostrar_spellcard = True
                cambio_fase()
                spellcard_balas() 
        elif fase == 3:
            if not nueva_fase:
                if vida_max > 70:
                    rotacion_bala_personalizada(10, ronald.pos, 12, "bala", 6, 0, 5)
                    rotacion_bala_personalizada_2(8, ronald.pos, 12, "bala", 5, 0, 3)
                    movimiento_avanzado(0, 0.02, 0, 0)
                    daño_golpe_cambio(0.8)
                elif 0 < vida_max <= 70:
                    titulo_spellcard(True)
                    if vida_max > 65:
                        spellcard_fallida = False
                        spellcard.play()
                        spellcard_balas()
                        vida_max = 64
                    if spell:
                        movimiento_avanzado(1, 0.03, 244, 90)
                        contador_tiempo = 0
                        tiempo_limite = tiempo_spellcards[fase-1]
                        spell = spellcard_ronald(spell)
                        daño = -40
                    if not spell:
                        movimiento_avanzado(180, 0.01, 0, 0)
                        rotacion_bala_personalizada(30, ronald.pos, 15, "papa", 3, 0, 5)
                        bonus_score(True)
                        daño_golpe_cambio(3)
                        papas_caida(30)
                        papas_lado(30)
                        tomate_caida(120)
                        tomate_lado(120)
                elif vida_max <= 0:
                    bonus.play()
                    bonus_score(False)
                    titulo_spellcard(False)
                    tiempo_limite = tiempo_normal[fase]
                    contador_movimiento = 0
                    vida_max = 0
                    contador_suma = 0
                    nueva_fase = True
            else:
                mostrar_spellcard = True
                cambio_fase()
                spellcard_balas()
        elif fase == 4:
            if not nueva_fase:
                if vida_max > 70:
                    tiempo_contador(1)
                    #rotacion_bala_personalizada(8, ronald.pos, 14, "bala", 3, 0, 6)
                    #rotacion_bala_personalizada_2(8, ronald.pos, 14, "bala", 6, 0, 3)
                    rotacion_bala_personalizada_dirigida(20, ronald.pos, 8, "bala", 0, 7, jugador, ronald, 6, 5)
                    movimiento_avanzado(0, 0.02, 0, 0)
                    daño_golpe_cambio(0.8)
                elif 0 < vida_max <= 70:
                    if vida_max > 65:
                        spellcard_fallida = False
                        spellcard.play()
                        spellcard_balas()
                        vida_max = 64
                    if spell:
                        contador_tiempo = 0
                        tiempo_limite = tiempo_spellcards[fase-1]
                        spell = spellcard_ronald(spell)
                        daño = -40
                    if not spell:
                        #ripples(50*(3-(vida_max/160)), 88, 1.5, "nugget", ronald.pos, jugador, ronald, 1)
                        #ripples_2(180, 36, 3, "papa", ronald.pos, jugador, ronald, 0)
                        #ripples_3(60, 4, 3, "tomate", ronald.pos, jugador, ronald, 2)
                        daño_golpe_cambio(3)
                elif vida_max <= 0:
                    bonus.play()
                    bonus_score(False)
                    titulo_spellcard(False)
                    tiempo_limite = tiempo_normal[fase]
                    contador_movimiento = 0
                    vida_max = 0
                    contador_suma = 0
                    nueva_fase = True
            else:
                mostrar_spellcard = True
                cambio_fase()
                spellcard_balas()
        elif fase == 8:
            if vida_max > 0:
                if vida_max > 319:
                    vida_max = 318
                    spellcard_fallida = False
                    spellcard.play()
                    spellcard_balas()
                if spell:
                    spell = spellcard_ronald(spell)
                    daño = 0
                if not spell:
                    daño_golpe_cambio(3)
                    mult = ((vida_max/320) + 1 )
                    mult_vel = ((-3/640)*vida_max)
                    ripples(int(80*mult), 54, mult_vel + 2.5, "nugget", ronald.pos, jugador, ronald, 1)
                    ripples_2(int(90*mult), 27, mult_vel + 3, "papa", ronald.pos, jugador, ronald, 0)
                    ripples_3(int(110*mult), 6, mult_vel + 4, "tomate", ronald.pos, jugador, ronald, 2)
                    # print(contador_rip_1, contador_rip_2, contador_rip_3)
            else:
                spellcard_balas()
            
    
    for mini in dispersados:
        if not pausa:
            mini[0].x += 10 * mini[1][0]
            mini[0].y -= 10 * mini[1][1]
            if mini[0].colliderect(ronald):
                daño += 0.5
                puntuacion += 30
                dispersados.remove(mini)
            if not mini[0].colliderect(rango_visible):
                dispersados.remove(mini)

    for cosa in bala_circular:
        if not pausa:
            cosa[0].y += 5 * cosa[1][1]
            cosa[0].x += 5 * cosa[1][0]
            cosa[2].y += 5 * cosa[1][1]
            cosa[2].x += 5 * cosa[1][0]

    for cosa in circulos_wa:
        if not pausa:
            cosa[0].y += cosa[3] * cosa[1][1]
            cosa[0].x += cosa[3] * cosa[1][0]
            cosa[2].y += cosa[3] * cosa[1][1]
            cosa[2].x += cosa[3] * cosa[1][0]

    for rip in Ripp:
        if not pausa:
            if not rip[2].colliderect(rango_visible):
                Ripp.remove(rip)
            rip[0].y += rip[3] * rip[1][1]
            rip[0].x += rip[3] * rip[1][0]
            rip[2].y += rip[3] * rip[1][1]
            rip[2].x += rip[3] * rip[1][0]
            if rip[2].x < 24:
                if rip[4] > 0:
                    rip[1][0] = -rip[1][0]
                    rip[4] -= 1
                    angle = int(math.degrees(math.atan2(rip[1][1], rip[1][0])))
                    rip[0].angle = -angle -90
            if rip[2].x > 465:
                if rip[4] > 0:
                    rip[1][0] = -rip[1][0]
                    rip[4] -= 1
                    angle = int(math.degrees(math.atan2(rip[1][1], rip[1][0])))
                    rip[0].angle = -angle -90
            if rip[2].y < 18:
                if rip[4] > 0:
                    rip[1][1] = -rip[1][1]
                    rip[4] -= 1
                    angle = int(math.degrees(math.atan2(rip[1][1], rip[1][0])))
                    rip[0].angle = -angle -90
            #if rip[2].y > 582:
             #   if rip[4] > 0:
              #      rip[1][1] = -rip[1][1]
               #     rip[4] -= 1
                #    angle = int(math.degrees(math.atan2(rip[1][1], rip[1][0])))
                 #   rip[0].angle = -angle -90


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
                ran[3] -= 0.1
                ran[0].x += ran[3]
                ran[2].x += ran[3]
                if ran[0].x < 20 and ran[3] < 0:
                    ran_ran_ru_inicio.remove(ran)
                    ran_exposure(20, y, ran[1])
            elif ran[1] == 2:
                y = ran[0].y          
                ran[3] -= 0.1
                ran[0].x -= ran[3]
                ran[2].x -= ran[3]
                if ran[0].x > 468 and ran[3] < 0:
                    ran_ran_ru_inicio.remove(ran)
                    ran_exposure(468, y, ran[1])

            elif ran[1] == 3:
                x = ran[0].x
                ran[3] -= 0.1
                ran[0].y += ran[3]
                ran[2].y += ran[3]
                if ran[0].y < 14 and ran[3] < 0:
                    ran_ran_ru_inicio.remove(ran)
                    ran_exposure(x, 14, ran[1])
            else:
                x = ran[0].x
                ran[3] -= 0.1
                ran[0].y -= ran[3]
                ran[2].y -= ran[3]
                if ran[0].y > 586 and ran[3] < 0:
                    ran_ran_ru_inicio.remove(ran)
                    ran_exposure(x, 586, ran[1])
                    
    for ran in ran_bala:
        if not pausa:
            for ran_2 in ran_bala:
                if ran[0].colliderect(ran_2[0]):
                    if ran != ran_2:
                        if ran[4] != 0 and ran_2[4] != 0:
                            if ran[3] in (1, 2):
                                ran[1][1] = 0
                                ran_2[1][1] = 0
                            else:
                                ran[1][0] = 0
                                ran_2[1][0] = 0
            if ran[4] == 1:
                ran_balas_grupo_1.append(ran)
            elif ran[4] == 2:
                ran_balas_grupo_2.append(ran)

            if ran[3] in (1 ,2):
                ran[0].x += ran[1][0] * 6
                ran[0].y += ran[1][1] * 3
                ran[2].x += ran[1][0] * 6
                ran[2].y += ran[1][1] * 3
            else:
                ran[0].x += ran[1][0] * 3
                ran[0].y += ran[1][1] * 6
                ran[2].x += ran[1][0] * 3
                ran[2].y += ran[1][1] * 6

            if ran[3] == 2:
                if ran[0].x < 20: 
                    if ran in ran_bala:
                        ran_bala.remove(ran)
            if ran[3] == 1:
                if ran[0].x > 468: 
                    if ran in ran_bala:
                        ran_bala.remove(ran)
            if ran[3] == 4:
                if ran[0].y < 9: 
                    if ran in ran_bala:
                        ran_bala.remove(ran)
            if ran[3] == 3:
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
                constante_pausa += rebote_pausa*0.7
            if menu_pausa.x >= 246:
                rebote_pausa += 1
                constante_pausa = -constante_pausa/1.8
        else:
            menu_pausa.x = 244
    else:
        menu_pausa.x = -202
        constante_pausa = 23
        rebote_pausa = 0

    if pausa:
        pygame.mixer.pause()
        music.pause()
    else:
        pygame.mixer.unpause()
        music.unpause()

    for ro in ron_bala:
        if not pausa:
            ro[1] += 3
            ro[0].x = ro[3] + math.sin(math.radians(ro[1])) * 10
            ro[0].y += 2
            ro[2].x = ro[3] + math.sin(math.radians(ro[1])) * 10
            ro[2].y += 2
            if ro[0]. y > 594:
                ron_bala.remove(ro)
            
    for al in ald_bala:
        if not pausa:
            al[1] += 3
            al[0].y = al[3] + math.sin(math.radians(al[1])) * 10
            al[0].x -= 2
            al[2].y = al[3] + math.sin(math.radians(al[1])) * 10
            al[2].x -= 2
            if al[0]. x < 11:
                ald_bala.remove(al)
    for cajas in cajitas_feliz:
        if not pausa:
            dist_x = cajas[1][0] - cajas[2].x
            dist_y =  cajas[1][1] - cajas[2].y 
            if dist_y < 0:
                multiy = -1
            elif dist_y > 0:
                multiy = 1
            else:
                multiy = 0
            if dist_x < 0:
                multix = -1
            elif dist_x > 0:
                multix = 1
            else:
                multix = 0
            #print(cajas[2].pos, cajas[1], cajas[4], (dist_x, dist_y), (0 < abs(dist_y) <= 30 and 0 < abs(dist_x) <= 30), (abs(dist_y) > 30 or abs(dist_x) > 30), (abs(dist_y) < 0.8 and abs(dist_x) < 0.8))
            if (0 <= abs(dist_y) <= 30 and 0 <= abs(dist_x) <= 30) and not (abs(dist_y) < 0.8 and abs(dist_x) < 0.8):
                cajas[0].y += dist_y/10 + 0.11*multiy
                cajas[2].y += dist_y/10 + 0.11*multiy
                cajas[0].x += dist_x/10 + 0.11*multix
                cajas[2].x += dist_x/10 + 0.11*multix
            elif abs(dist_y) > 30 or abs(dist_x) > 30:
                cajas[0].y -= cajas[4][1]/80
                cajas[2].y -= cajas[4][1]/80
                cajas[0].x -= cajas[4][0]/80
                cajas[2].x -= cajas[4][0]/80
            elif abs(dist_y) < 0.8 and abs(dist_x) < 0.8:
                cajas[0].y = cajas[1][1]
                cajas[2].y = cajas[1][1]
                cajas[0].x = cajas[1][0]
                cajas[2].x = cajas[1][0]
                rotacion_bala_personalizada(1, cajas[2].pos, 3, "nugget", -13, cajas[3], 7)
                cajas[3] += 1
                if cajas[3] >=  72:
                    cajitas_feliz.remove(cajas)
    for punto in puntos:
        if not pausa:
            if punto[1] < 20:
                punto[0].y -= 10 - punto[1]/2
                punto[1] += 1
            else:
                teledirigir_balas(punto[0], 10 , jugador)
            if punto[0].colliderect(jugador):
                tick.play()
                puntuacion += 100
                puntos.remove(punto)
    for papa in papas:
        if not pausa:
            if papa[3] == 0:
                papa[0].y += 3
                papa[2].y += 3
                if not papa[2].colliderect(rango_visible):
                    papas.remove(papa)
            else:
                papa[0].x -= 3
                papa[2].x -= 3
                if not papa[2].colliderect(rango_visible):
                    papas.remove(papa)

    for tomate in tomates:
        if not pausa: 
            if tomate[3] == 0:
                tomate[0].y += tomate[1]*3
                tomate[2].y += tomate[1]*3
                if tomate[2].y > 585:
                    tomate[0].y = 7
                    tomate[2].y = 7
                    tomate[1] += 1
                if tomate[1] == 4:
                    tomates.remove(tomate)
            else: 
                tomate[0].x -= tomate[1]*3
                tomate[2].x -= tomate[1]*3
                if tomate[2].x < 25:
                    tomate[0].x = 476
                    tomate[2].x = 476
                    tomate[1] += 1
                if tomate[1] == 4:
                    tomates.remove(tomate)
def mover_jugador(direccion, distancia, shift):
    if not pausa:
        if focus:
            distancia = shift
        if (direccion == 'up'):
            jugador.y -= distancia
            hitbox.y -= distancia
            gracia.y -= distancia
        if (direccion == 'right'):
            jugador.x += distancia
            hitbox.x += distancia
            gracia.x += distancia
        if (direccion == 'down'):
            jugador.y += distancia
            hitbox.y += distancia
            gracia.y += distancia
        if (direccion == 'left'):
            jugador.x -= distancia
            hitbox.x -= distancia
            gracia.x -= distancia
    if (jugador.y <= 26):
        jugador.y = 26
        hitbox.y = 26
        gracia.y = 26
    if (jugador.x <= 31):
        jugador.x = 31
        hitbox.x = 31
        gracia.x = 31
    if (jugador.y >= 574):
        jugador.y = 574
        hitbox.y = 574
        gracia.y = 574
    if (jugador.x >= 458):
        jugador.x = 458
        hitbox.x = 458
        gracia.x = 458
def disparo():
    global contador, contador_extra, poder_bala, puntuacion, espera_bala, espera_extra
    if build == 1:
        if not pausa:
            if not focus:
                contador += 1
                if contador == espera_bala:
                    contador = 0
                    bala = Actor("bala_"+str(poder_bala), (jugador.x, jugador.y))
                    cuchillo = Actor('cuchillos', (jugador.x+5 , jugador.y))
                    cuchillo2 = Actor('cuchillos', (jugador.x-5, jugador.y))
                    atras = (bala, 0, 1)
                    delante_1 = (cuchillo, 1, 0)
                    delante_2 = (cuchillo2, 1, 0)
                    balas.append(delante_1)
                    balas.append(delante_2)
                    balas.append(atras)
                    puntuacion += 500
                    bala_1_sfx.play()
            else:
                if not super_knifes:
                    contador += 1
                    if contador == espera_bala:
                        contador = 0
                        bala_5 = Actor('bala_'+str(poder_bala), (jugador.x+8 , jugador.y))
                        bala_4 = Actor('bala_'+str(poder_bala), (jugador.x-8, jugador.y))
                        cuchillo = Actor('cuchillos', (jugador.x , jugador.y))
                        bala = Actor('bala_'+str(poder_bala), (jugador.x, jugador.y))
                        bala_2 = Actor('bala_'+str(poder_bala), (jugador.x , jugador.y ))
                        bala_3 = Actor("bala_"+str(poder_bala), (jugador.x , jugador.y ))
                        delante_1 = (bala_4, 1, 0)
                        delante_3 = (bala_5, 1, 0)
                        delante_2 = (cuchillo, 1, 0)
                        atras_1 = (bala, 0, 0)
                        atras_2 = (bala_2, 0, 1)
                        atras_3 = (bala_3, 0, 2)
                        balas.append(atras_1)
                        balas.append(atras_2)
                        balas.append(atras_3)
                        balas.append(delante_1)
                        balas.append(delante_2)
                        balas.append(delante_3)
                        puntuacion += 1500
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
                    puntuacion += 100
                    bala_2_sfx.play(1)
                if contador_extra >= espera_extra/poder_bala:
                    contador_extra = 0
                    burbuja_sfx.play()
                    puntuacion += 150
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
                    puntuacion += 700
    elif build == 3:
        if not pausa:
            if not focus:
                contador += 1
                if contador == espera_bala:
                    contador = 0
                    atomo = Actor('atom', (jugador.x+10, jugador.y -9))
                    atomo_2 = Actor('atom', (jugador.x-10, jugador.y -9))
                    balas.append(atomo)
                    balas.append(atomo_2)
                    puntuacion += 600
                    bala_3_sfx.play()
                
def verificar_rango(objeto):
    if not build == 1:
        if not rango_visible.colliderect(objeto):
            if objeto in balas:
                balas.remove(objeto)
            if objeto in dispersados:
                dispersados.remove(objeto)
    else:
        if not rango_visible.colliderect(objeto[0]):
            balas.remove(objeto)

def seno_random(valor):
    y = math.sin(math.radians(valor))
    if valor > 90:
        x = 1 - y
    elif valor < 90:
        x =  (-y + 1)*-1
    else:
        x = 0 
    return round(x, 2), round(y, 2)

def bala_spin(cadencia):   
    global numero
    global contador_enemigo
    if not pausa:
        contador_enemigo += 1
        if contador_enemigo >= cadencia:
            contador_enemigo = 0
            for random in range(0, 360, 60):
                nuevo = numero + random
                y = math.sin(math.radians(nuevo))
                x = math.cos(math.radians(nuevo))
                coord = (x, y)
                balas = Actor("bala.png", ronald.pos)
                hitbox_bala = Actor("bala_hitbox.png", ronald.pos)
                todo = (balas, coord, hitbox_bala)
                bala_circular.append(todo)
            numero += 14

def bala_circulos(cadencia):
    global numero_2
    global contador_enemigo_2
    if not pausa:
        contador_enemigo_2 += 1
        if contador_enemigo_2 >= cadencia:
            contador_enemigo_2 = 0
            for a in range(18):
                numero_2 += 20
                y = math.sin(math.radians(numero_2))
                x = math.cos(math.radians(numero_2))
                coord = (x, y)
                bala = Actor("bala.png", ronald.pos)
                bala.angle = -angle -90
                hitbox_bala = Actor("bala_hitbox.png", ronald.pos)
                todo = (bala, coord, hitbox_bala, 5)
                circulos_wa.append(todo)
            numero_2 += 10

def rotacion_bala_personalizada(cadencia, posicion, rango, sprite, variacion, contador_personalizado, velocidad_personalizada):
    global numero_2
    global contador_enemigo_2
    if not pausa:
        if contador_personalizado == 0:
            contador_enemigo_2 += 1
        else:
            contador_enemigo_2 = contador_personalizado
        if (contador_enemigo_2 % cadencia) == 0:
            contador_enemigo_2 = 0
            for a in range(rango):
                numero_2 += 360/rango
                y = math.sin(math.radians(numero_2))
                x = math.cos(math.radians(numero_2))
                coord = (x, y)
                angle = int(math.degrees(math.atan2(y, x)))
                bala = Actor(sprite + ".png", posicion)
                bala.angle = -angle -90
                hitbox_bala = Actor(sprite+"_hitbox.png", posicion)
                todo = (bala, coord, hitbox_bala, velocidad_personalizada)
                circulos_wa.append(todo)
            numero_2 += variacion

def rotacion_bala_personalizada_2(cadencia, posicion, rango, sprite, variacion, contador_personalizado, velocidad_personalizada):
    global numero
    global contador_enemigo
    if not pausa:
        if contador_personalizado == 0:
            contador_enemigo += 1
        else:
            contador_enemigo = contador_personalizado
        if (contador_enemigo % cadencia) == 0:
            contador_enemigo = 0
            for a in range(rango):
                numero += 360/rango
                y = math.sin(math.radians(numero))
                x = math.cos(math.radians(numero))
                coord = (x, y)
                angle = int(math.degrees(math.atan2(y, x)))
                bala = Actor(sprite + ".png", posicion)
                bala.angle = - angle
                hitbox_bala = Actor(sprite+"_hitbox.png", posicion)
                todo = (bala, coord, hitbox_bala, velocidad_personalizada)
                circulos_wa.append(todo)
            numero += variacion
def rotacion_bala_personalizada_dirigida(cadencia, posicion, rango, sprite, contador_personalizado, velocidad_personalizada, objetivo, objeto, constante_decrecion, numero_decrecion):
    global numero_3
    global contador_enemigo_3
    if not pausa:
        if contador_personalizado == 0:
            contador_enemigo_3 += 1
        else:
            contador_enemigo_3 = contador_personalizado
        if (contador_enemigo_3 % cadencia) == 0:
            contador_enemigo_3 = 0
            tele_x = objetivo.x - objeto.x
            tele_y = objetivo.y - objeto.y
            numero_3 = math.degrees(math.atan2(tele_y, tele_x))
            for a in range(rango):
                numero_3 += 360/rango
                for numero_actual in range(numero_decrecion):
                    vel_decrecion = constante_decrecion/(constante_decrecion+numero_actual)
                    y = math.sin(math.radians(numero_3)) * vel_decrecion
                    x = math.cos(math.radians(numero_3)) * vel_decrecion
                    coord = (x, y)
                    angle = int(math.degrees(math.atan2(y, x)))
                    bala = Actor(sprite + ".png", posicion)
                    bala.angle = - angle
                    hitbox_bala = Actor(sprite+"_hitbox.png", posicion)
                    todo = (bala, coord, hitbox_bala, velocidad_personalizada)
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
    for a in range(numero_de_bombas):
        bomba_appendar = Actor("bomba_sprite.png", (499+a*25, 90))
        numero_bombas.append(bomba_appendar)

def movimiento_avanzado(cooldown, mov, x_fija, y_fija):
    global contador_movimiento, validacion_1 ,validacion_2, temporizador_movimiento, dif_x, dif_y, x, y
    if not pausa:
        # print(cooldown, temporizador_movimiento, contador_movimiento, temporizador_movimiento <= contador_movimiento, x, y, ronald.x, ronald.y, dif_x, dif_y)
        if validacion_1 and validacion_2:
                temporizador_movimiento = 1
                contador_movimiento = cooldown
                dif_x = 0
                dif_y = 0
                x = 0
                y = 0
                validacion_1 = False
                validacion_2 = False
        if cooldown == 0:
            if contador_movimiento == 0:
                contador_movimiento = randint(150, 300)
        else:
            contador_movimiento = cooldown
        #print(not((x_fija != 0 or y_fija != 0) and (temporizador_movimiento > 1)))
        # print((temporizador_movimiento == 4), not (temporizador_movimiento == 4))
        if  (x_fija != 0 or y_fija != 0):
            x = x_fija
            y = y_fija
            if not temporizador_movimiento == 4:
                dif_x = (x - ronald.x)
                dif_y = (y - ronald.y)
                temporizador_movimiento = 4
                contador_movimiento = 1
        if temporizador_movimiento <= contador_movimiento:
            temporizador_movimiento += 1
            if x == 0 and y == 0:
                x = randint(42, 439)
                y = randint(34,160)
                dif_x = round(x - ronald.x)
                dif_y = round(y - ronald.y)

        else:
            #print((x, round(ronald.x), dif_x), (y, round(ronald.y), dif_y), (validacion_1, validacion_2))
            if dif_x < 0:
                if not round(ronald.x) <= x:
                    ronald.x += mov*dif_x
                else:
                    validacion_1 = True    
            elif dif_x > 0:
                if not round(ronald.x) >= x:
                    ronald.x += mov*dif_x
                else:
                    validacion_1 = True
            else:
                validacion_1 = True
            if dif_y < 0:
                if not round(ronald.y) <= y:
                    ronald.y += mov*dif_y
                else:
                    validacion_2 = True
            elif dif_y > 0:
                if not round(ronald.y) >= y:
                    ronald.y += mov*dif_y
                else:
                    validacion_2 = True
            else:
                validacion_2 = True

def movimiento_circular(centro, x_max, y_max, velocidad, vueltas):
    global contador_movimiento_circular, direccion_movimiento_circular
    if not pausa:
        # contador_movimiento_circular += 1
        #print(contador_movimiento_circular, contador_movimiento_circular >= (contador_movimiento_circular*vueltas - 30*vueltas))
        if 360>= contador_movimiento_circular >= (360*vueltas - 30*vueltas):
            contador_movimiento_circular += (30-(contador_movimiento_circular-330*vueltas))/30 +0.05
        elif 360*vueltas + 360*30 >= contador_movimiento_circular >= 360*vueltas:
            contador_movimiento_circular += 360
        elif contador_movimiento_circular >= 360*vueltas + 360*30:
            direccion_movimiento_circular = -direccion_movimiento_circular
            contador_movimiento_circular = 0
        else:
            contador_movimiento_circular += 1
        ronald.x = centro[0] + x_max * math.cos(math.radians(contador_movimiento_circular*velocidad))
        ronald.y = centro[1] - y_max * math.sin(math.radians(contador_movimiento_circular*velocidad)) * direccion_movimiento_circular

def cambio_bala(comprobante):
    global poder_bala, contador_cambio_bala, contador_extra, puntuacion
    if build == 1:
        if not pausa:
            if comprobante:
                puntuacion += 3
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
                puntuacion += 4
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
                        puntuacion += 1
                        poder_bala = 1
                    elif 180 < contador_cambio_bala <= 300:
                        puntuacion += 3
                        poder_bala = 2
                    elif 300 <contador_cambio_bala:
                        puntuacion += 5
                        poder_bala = 3
                else:
                    if poder_bala > 0:
                        misil(poder_bala)
                    puntuacion += 1500*poder_bala
                    poder_bala = 0
                    contador_cambio_bala = 0

def teledirigir_balas(objeto, velocidad, objetivo):
    if not pausa:
        global tele_x, tele_y, hipo, mov_x, mov_y
        tele_x = objetivo.x - objeto.x
        tele_y = objetivo.y - objeto.y
        hipo = math.sqrt(tele_x ** 2 + tele_y ** 2)

        if hipo != 0:
            mov_x = tele_x * velocidad / hipo
            mov_y = tele_y * velocidad / hipo
        
        objeto.x +=  mov_x
        objeto.y +=  mov_y
        if build == 3:
            angulo = math.degrees(math.atan2(-tele_y, tele_x))
            if mov_x != 0:
                objeto.angle = angulo-90
            elif tele_x == 0 and tele_y < 0:
                objeto.angle = 0
            else:
                objeto.angle = 180

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
                x = 468
            elif numero == 3:
                x = randint(73, 468)
                y = 27
            else:
                x = randint(73, 468)
                y = 573
            balas = Actor("mc_bala", (x, y))
            hitbox = Actor("bala_hitbox", (x, y))
            velo = 3
            todo = [balas, numero, hitbox, velo]
            ran_ran_ru_inicio.append(todo)
                
def ran_exposure(x, y, direccion):
    if not pausa:
        if direccion == 1: #Izquierda
            ran_ran_ru_sfx.play()
            for _ in range(141):
                if _ in (5, 15, 20, 25, 35, 40):
                    balas_ran1 = Actor("mc_bala", (x-_*5, y - 6*_))
                    balas_ran2 = Actor("mc_bala", (x-_*5, y + 6*_))
                    hitbox_1 = Actor("bala_hitbox", (x-_*5, y - 6*_))
                    hitbox_2 = Actor("bala_hitbox", (x-_*5, y + 6*_))
                    vel = (1 , 1.1)
                    vel2 = (1 , -1.1)
                    trio_1 = (balas_ran1, vel, hitbox_1, direccion, 0)
                    trio_2 = (balas_ran2, vel2, hitbox_2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (50, 55, 65, 70, 80):
                    balas_ran1 = Actor("mc_bala", (x-_*5, y - 3*_))
                    balas_ran2 = Actor("mc_bala", (x-_*5, y + 3*_))
                    hitbox_1 = Actor("bala_hitbox", (x-_*5, y - 3*_))
                    hitbox_2 = Actor("bala_hitbox", (x-_*5, y + 3*_))
                    vel = [1 , 0.7]
                    vel2 = [1 , -0.7]
                    trio_1 = [balas_ran1, vel, hitbox_1, direccion, 1]
                    trio_2 = [balas_ran2, vel2, hitbox_2, direccion, 2]
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (90, 95, 105, 110, 120, 125, 135, 140):
                    balas_ran1 = Actor("mc_bala", (x-_*5, y - 40))
                    balas_ran2 = Actor("mc_bala", (x-_*5, y + 40))
                    hitbox_1 = Actor("bala_hitbox", (x-_*5, y - 40))
                    hitbpx_2 = Actor("bala_hitbox", (x-_*5, y + 40))
                    vel = (1 , 0)
                    vel2 = (1 , 0)
                    trio_1 = (balas_ran1, vel, hitbox_1, direccion, 0)
                    trio_2 = (balas_ran2, vel2, hitbox_2, direccion, 0)
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
                    hitbox_1 = Actor("bala_hitbox", (x+_*5, y - 6*_))
                    hitbox_2 = Actor("bala_hitbox", (x+_*5, y +6*_))
                    trio_1 = (balas_ran1, vel, hitbox_1, direccion, 0)
                    trio_2 = (balas_ran2, vel2, hitbox_2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (50, 55, 65, 70, 80):
                    balas_ran1 = Actor("mc_bala", (x+_*5, y - 3*_))
                    balas_ran2 = Actor("mc_bala", (x+_*5, y + 3*_))
                    hitbox_1 = Actor("bala_hitbox", (x+_*5, y - 3*_))
                    hitbox_2 = Actor("bala_hitbox", (x+_*5, y + 3*_))   
                    vel = [-1 , 0.7]
                    vel2 = [-1 , -0.7]
                    trio_1 = [balas_ran1, vel, hitbox_1, direccion, 1]
                    trio_2 = [balas_ran2, vel2, hitbox_2, direccion, 2]
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (90, 95, 105, 110, 120, 125, 135, 140):
                    balas_ran1 = Actor("mc_bala", (x+_*5, y - 40))
                    balas_ran2 = Actor("mc_bala", (x+_*5, y + 40))
                    hitbox_1 = Actor("bala_hitbox", (x+_*5, y - 40))
                    hitbox_2 = Actor("bala_hitbox", (x+_*5, y + 40))
                    vel = (-1 , 0)
                    vel2 = (-1 , 0)
                    trio_1 = (balas_ran1, vel, hitbox_1, direccion, 0)
                    trio_2 = (balas_ran2, vel2, hitbox_2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
        elif direccion == 3: #Abajo
            ran_ran_ru_sfx.play()
            for _ in range(141):
                if _ in (5, 15, 20, 25, 35, 40):
                    balas_ran1 = Actor("mc_bala", (x + 6 * _, y - _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 6 * _, y - _ * 5))
                    hitbox_1 = Actor("bala_hitbox", (x + 6 * _, y - _ * 5))
                    hitbox_2 = Actor("bala_hitbox", (x - 6 * _, y - _ * 5))
                    vel = (-1.1 , 1)
                    vel2 = (1.1, 1)
                    trio_1 = (balas_ran1, vel, hitbox_1, direccion, 0)
                    trio_2 = (balas_ran2, vel2, hitbox_2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (50, 55, 65, 70, 80):
                    balas_ran1 = Actor("mc_bala", (x + 3 * _, y - _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 3 * _, y - _ * 5))
                    hitbox_1 = Actor("bala_hitbox", (x + 3 * _, y - _ * 5))
                    hitbox_2 = Actor("bala_hitbox", (x - 3 * _, y - _ * 5))
                    vel = [-0.7 , 1]
                    vel2 = [0.7 , 1]
                    trio_1 = [balas_ran1, vel, hitbox_1, direccion, 1]
                    trio_2 = [balas_ran2, vel2, hitbox_2, direccion, 2]
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (90, 95, 105, 110, 120, 125, 135, 140):
                    balas_ran1 = Actor("mc_bala", (x + 40, y - _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 40, y - _ * 5))
                    hitbox_1 = Actor("bala_hitbox", (x + 40, y - _ * 5))
                    hitbox_2 = Actor("bala_hitbox", (x - 40, y - _ * 5))
                    vel = (0 , 1)
                    vel2 = (0 , 1)
                    trio_1 = (balas_ran1, vel, hitbox_1, direccion, 0)
                    trio_2 = (balas_ran2, vel2, hitbox_2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
        else: #Arriba
            ran_ran_ru_sfx.play()
            for _ in range(141):
                if _ in (5, 15, 20, 25, 35, 40):
                    balas_ran1 = Actor("mc_bala", (x + 6 * _, y + _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 6 * _, y + _ * 5))
                    hitbox_1 = Actor("bala_hitbox", (x + 6 * _, y + _ * 5))
                    hitbox_2 = Actor("bala_hitbox", (x - 6 * _, y + _ * 5)) 
                    vel = (-1.1 , -1)
                    vel2 = (1.1, -1)
                    trio_1 = (balas_ran1, vel, hitbox_1, direccion, 0)
                    trio_2 = (balas_ran2, vel2, hitbox_2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (50, 55, 65, 70, 80):
                    balas_ran1 = Actor("mc_bala", (x + 3 * _, y + _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 3 * _, y + _ * 5))
                    hitbox_1 = Actor("bala_hitbox", (x + 3 * _, y + _ * 5))
                    hitbox_2 = Actor("bala_hitbox", (x - 3 * _, y + _ * 5))
                    vel = [-0.7 , -1]
                    vel2 = [0.7 , -1]
                    trio_1 = [balas_ran1, vel, hitbox_1, direccion, 1]
                    trio_2 = [balas_ran2, vel2, hitbox_2, direccion, 2]
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)
                if _ in (90, 95, 105, 110, 120, 125, 135, 140):
                    balas_ran1 = Actor("mc_bala", (x + 40, y + _ * 5))
                    balas_ran2 = Actor("mc_bala", (x - 40, y + _ * 5))
                    hitbox_1 = Actor("bala_hitbox", (x + 40, y + _ * 5))
                    hitbox_2 = Actor("bala_hitbox", (x - 40, y + _ * 5))
                    vel = (0 , -1)
                    vel2 = (0 , -1)
                    trio_1 = (balas_ran1, vel, hitbox_1, direccion, 0)
                    trio_2 = (balas_ran2, vel2, hitbox_2, direccion, 0)
                    ran_bala.append(trio_1)
                    ran_bala.append(trio_2)

def ron():
    global ron_contador
    if not pausa:
        ron_contador += 1
        if ron_contador >= 60:
            ron_contador = 0
            for x in range(31, 438, 58):
                va = x
                bala_mov = Actor("bala_azul.png", (x , 7))
                hitbox_bala = Actor("bala_hitbox.png", (x , 7))
                dio = [bala_mov, 0, hitbox_bala, va]
                ron_bala.append(dio)

def ald():
    global ald_contador
    if not pausa:
        ald_contador += 1
        if ald_contador >= 90:
            ald_contador = 0
            for y in range(26, 576, 61):
                va = y
                bala_mov = Actor("bala_azul.png", (476 , y))
                hitbox_bala = Actor("bala_hitbox.png", (476 , y))
                dio = [bala_mov, 0, hitbox_bala, va]
                ald_bala.append(dio)

def limpiar_pantalla():
    if not pausa:
        for lista in todas_las_balas_enemigas:
            lista.clear()
def spellcard_balas():
    if not pausa:
        for lista in todas_las_balas_enemigas:
            puntos_spellcard(lista)
            lista.clear()

def spellcard_ronald(Comprobante):
    if not pausa: 
        if Comprobante:
            if int(imagen.x) in range(191, 251):
                imagen.x -= 1
                imagen.y += 0.5
            else:
                imagen.x -= 16
                imagen.y += 8
            if not imagen.colliderect(rango_visible) and imagen.x < 30:
                return False
            else:
                return True
        else:
            imagen.x = 800
            imagen.y = 0
def cambio_fase():
    global fase, vida_max, nueva_fase, vida_verde, spell
    if not pausa:
        vida_max += 4
        spellcard_ronald(False)
        vida_verde = Rect((65, 25), (vida_max, 10))
        if vida_max >= 319:
            vida_max = 320
            fase += 1
            nueva_fase = False
            spell = True

def cajitas(cadencia):
    global contador_cajitas
    if not pausa: 
        contador_cajitas += 1
        if contador_cajitas >= cadencia:
            contador_cajitas = 0
            x = jugador.x
            y = jugador.y
            x_dif = round(ronald.x - jugador.x)
            y_dif = round(ronald.y - jugador.y)
            coord = (x, y)
            coord_dif = (x_dif, y_dif)
            y = 20
            cajita = Actor("cajita_feliz.png", ronald.pos)
            cajita_hitbox = Actor("cajita_hitbox", ronald.pos)
            contador = 0
            todo = [cajita, coord, cajita_hitbox, contador, coord_dif]
            cajitas_feliz.append(todo)

def puntos_spellcard(lista):
    global puntuacion
    if not pausa:
        for balas in lista:
            punto = Actor("hitbox.png", balas[0].pos)
            todo = [punto, 0]
            puntos.append(todo)
            puntuacion += 100

def papas_caida(cadencia):
    global contador_papas
    if not pausa:
        contador_papas += 1
        if contador_papas >= cadencia:
            contador_papas = 0
            ataque_5.play()
            for x in range(34, 441, 58):
                papa = Actor("papa.png", (x , 7))
                papa_hitbox = Actor("papa_hitbox.png", (x , 7))
                todo = [papa, "relleno", papa_hitbox, 0]
                papas.append(todo)

def tomate_caida(cadencia):
    global contador_tomate, tomate_dire
    if not pausa:
        if tomate_dire == 0:
            contador_tomate += 1
            if (contador_tomate % cadencia) == 0:
                contador_tomate = 0
                tomate_dire = 1
                zona = ((jugador.x - 31) // 58 )+ 1
                if zona > 7:
                    zona = 7
                x = (58 * zona) + 5
                tomate = Actor("tomate.png", (x, 7))
                tomate_hitbox = Actor("tomate_hitbox.png", (x, 7))
                todo = [tomate, 1 , tomate_hitbox, 0]
                tomates.append(todo)


def tomate_lado(cadencia):
    global contador_tomate_2, tomate_dire
    if not pausa:
        if tomate_dire == 1:
            contador_tomate_2 += 1
            if (contador_tomate_2 % cadencia) == 0:
                contador_tomate_2 = 0
                tomate_dire = 0
                zona = ((jugador.y - 31) // 58 )+ 1
                if zona < 1:
                    zona = 1
                y = (58 * zona) + 1
                tomate = Actor("tomate.png", (476, y))
                tomate.angle = 90
                tomate_hitbox = Actor("tomate_hitbox.png", (476, y))
                tomate_hitbox.angle = 90
                todo = [tomate, 1 , tomate_hitbox, 1]
                tomates.append(todo)
# 438 576, 476


def papas_lado(cadencia):
    global contador_papas_2
    if not pausa:
        contador_papas_2 += 1
        if contador_papas_2 >= cadencia:
            contador_papas_2 = 0
            ataque_5.play()
            for y in range(26, 576, 58):
                papa = Actor("papa.png", (476 , y))
                papa.angle = 90
                papa_hitbox = Actor("papa_hitbox.png", (476 , y))
                papa_hitbox.angle = 90
                todo = [papa, "relleno", papa_hitbox, 1]
                papas.append(todo)

def tiempo_contador(tipo):
    if not pausa:
        global contador_tiempo, tiempo_limite, vida_max, vida_verde
        contador_tiempo += 1
        if contador_tiempo >= 60:
            if tiempo_limite == 0:
                if tipo == 1:
                    vida_max = 70
                else:
                    vida_max = 0
                vida_verde = Rect((65, 25), (vida_max, 10))
            else:
                contador_tiempo = 0
                tiempo_limite -= 1
                if tiempo_limite <= 5:
                    beep.play()
def titulo_spellcard(Comprobante):
    global nombre_spellcard, contador_spellcard, spellcard_x, spellcard_y, spellcard_tamaño, spellcard_transparencia, spellcard_bonus_transparencia
    if not pausa:
        if Comprobante:
            contador_spellcard += 1
            if contador_spellcard <= 30:
                spellcard_x = 450
                spellcard_y = 530
                nombre_spellcard = lista_spellcards[fase-1]
                spellcard_tamaño = 105 - contador_spellcard*8/3
                spellcard_transparencia = (contador_spellcard/30) 
            elif 100 < contador_spellcard <= 125:
                spellcard_y = 503 - (contador_spellcard-100)*16
            elif 125 < contador_spellcard <= 145:
                spellcard_bonus_transparencia = (contador_spellcard-125)/20
                # spellcard_y = 60 + (((contador_spellcard-125)) * 2.15) - 43
                spellcard_y = 60 + 43*((1/(contador_spellcard-124))-0.04166666667)
            elif contador_spellcard > 145:
                spellcard_y = 60
        else:
            spellcard_bonus_transparencia = 0
            contador_spellcard = 0
            spellcard_x = 0
            spellcard_y = 0
            nombre_spellcard = ""
            spellcard_tamaño = 0
            spellcard_transparencia = 0

def bonus_score(comprobante):
    global contador_bonus, spellcard_bonus, spellcard_fallida
    if not pausa:
        if comprobante:
            if not spellcard_fallida:
                valor = lista_bonus[fase-1]
                contador_bonus += 1
                limite_bonus = (tiempo_spellcards[fase-1]+1) * 60
                porcentaje = (contador_bonus/limite_bonus) / 2
                spellcard_bonus = int(valor - valor*porcentaje)
            else:
                spellcard_bonus = "Fallido"
        else:
            contador_bonus = -1
            limite_bonus = 0
def agregar_bonus():
    global contador_suma, puntuacion, bonus_visible, bonus_visible_2, spellcard_fallida, spellcard_obtenido, mostrar_spellcard
    if not pausa:   
        contador_suma += 1
        if not spellcard_fallida:
            spellcard_obtenido = "Spellcard Bonus!"
            if contador_suma < 20:
                bonus_visible = contador_suma/20
                bonus_visible_2 = contador_suma/20
            elif 20 <= contador_suma < 160:
                bonus_visible = 1
                bonus_visible_2 = 1
        else:
            spellcard_obtenido = "Spellcard Fallida"
            if contador_suma < 20:
                bonus_visible = contador_suma/20
            elif 20 <= contador_suma < 160:
                bonus_visible = 1
        if contador_suma <= 60:
            mostrar_spellcard =  True
            if not spellcard_fallida:
                puntuacion += int(spellcard_bonus/60)
        elif 60 < contador_suma <= 160:
            mostrar_spellcard =  True
        elif 160 < contador_suma < 180:
            if not spellcard_fallida:
                bonus_visible = 1 - (contador_suma-160)/20
                bonus_visible_2 = 1 - (contador_suma-160)/20
        else:
            bonus_visible = False
            bonus_visible_2 = False
            mostrar_spellcard =  False
def fase_inicio():
    global fase
    if not fase >= 1:
        fase += 1

def musica_play():
    # print (music.is_playing("ronald.wav"), not music.is_playing("ronald.wav"))
    if not music.is_playing("ronald.wav"):
        music.play("ronald.wav")
        music.set_volume(0.2)

def cubo_dialogo_mov(num):
    if num == 1:
        if -30 < fase <= -10: #(244, 510) 41
            cubo_dialogo.y -= 5
        elif -10 < fase < 0:
            # print(fase, 10+fase, 1/(10+fase), 33*(1/(10+fase)))
            cubo_dialogo.y = 510 + 13*(1/(10+fase))
        elif fase == 0:
            cubo_dialogo.y = 510
    else:
        cubo_dialogo.y += 5
def dialogo_a_mostrar(texto):
    global dialogo, dialogo_op, color_dialogo
    if texto != "end":
        if dialogo != texto[0]:
            dialogo = texto[0]
            dialogo_op = 0
        if dialogo_op < 1:
            if keyboard.LCTRL:
                dialogo_op += 1/5
            else:
                dialogo_op += 1/20
        if texto[1] == 0:
            color_dialogo = "orange"
        else:
            if build == 1:
                color_dialogo = "red"
            elif build == 2:
                color_dialogo = "blue"
            else:
                color_dialogo = "green"
    else:
        dialogo = None
        if dialogo_op > 0:
            dialogo_op = 0
 
def ripples(cadencia, rango, velocidad_personalizada, sprite, posicion, objetivo, objeto, rebotes):
    global contador_rip_1
    if not pausa:
        contador_rip_1 += 1
        if (contador_rip_1 % cadencia) == 0:
            contador_rip_1 = 0
            tele_x = objetivo.x - objeto.x
            tele_y = objetivo.y - objeto.y
            numero_3 = math.degrees(math.atan2(tele_y, tele_x))
            x_pos = posicion[0] + randint(-50, 50)
            y_pos = posicion[1] + randint(-50, 50)
            posicion_ran = (x_pos, y_pos)
            for a in range(rango):
                numero_3 += 360/rango
                y = math.sin(math.radians(numero_3)) 
                x = math.cos(math.radians(numero_3))
                coord = [x, y]
                angle = int(math.degrees(math.atan2(y, x)))
                bala = Actor(sprite + ".png", posicion_ran)
                bala.angle = -angle -90
                hitbox_bala = Actor(sprite+"_hitbox.png", posicion_ran)
                hitbox_bala.angle = -angle -90
                todo = [bala, coord, hitbox_bala, velocidad_personalizada, rebotes]
                Ripp.append(todo)
def ripples_2(cadencia, rango, velocidad_personalizada, sprite, posicion, objetivo, objeto, rebotes):
    global contador_rip_2
    if not pausa:
        contador_rip_2 += 1
        if (contador_rip_2 % cadencia) == 0:
            contador_rip_2 = 0
            tele_x = objetivo.x - objeto.x
            tele_y = objetivo.y - objeto.y
            numero_3 = math.degrees(math.atan2(tele_y, tele_x))
            x_pos = posicion[0] + randint(-50, 50)
            y_pos = posicion[1] + randint(-50, 50)
            posicion_ran = (x_pos, y_pos)
            for a in range(rango):
                numero_3 += 360/rango
                y = math.sin(math.radians(numero_3)) 
                x = math.cos(math.radians(numero_3))
                coord = [x, y]
                angle = int(math.degrees(math.atan2(y, x)))
                bala = Actor(sprite + ".png", posicion_ran)
                bala.angle = -angle -90
                hitbox_bala = Actor(sprite+"_hitbox.png", posicion_ran)
                hitbox_bala.angle = -angle -90
                todo = [bala, coord, hitbox_bala, velocidad_personalizada, rebotes]
                Ripp.append(todo)

def ripples_3(cadencia, rango, velocidad_personalizada, sprite, posicion, objetivo, objeto, rebotes):
    global contador_rip_3
    if not pausa:
        contador_rip_3 += 1
        if (contador_rip_3 % cadencia) == 0:
            contador_rip_3 = 0
            tele_x = objetivo.x - objeto.x
            tele_y = objetivo.y - objeto.y
            numero_3 = math.degrees(math.atan2(tele_y, tele_x))
            for a in range(rango):
                numero_3 += 360/rango
                y = math.sin(math.radians(numero_3)) 
                x = math.cos(math.radians(numero_3))
                coord = [x, y]
                angle = int(math.degrees(math.atan2(y, x)))
                bala = Actor(sprite + ".png", posicion)
                bala.angle = - angle -90
                hitbox_bala = Actor(sprite+"_hitbox.png", posicion)
                hitbox_bala.angle = -angle -90
                todo = [bala, coord, hitbox_bala, velocidad_personalizada, rebotes]
                Ripp.append(todo)

pgzrun.go()