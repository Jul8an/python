from abc import ABC,abstractmethod
import time

class Personajes(ABC):
    def __init__(self, arma, armadura, ataque, defensa, vida, nombre):
        self.arma = arma
        self.armadura = armadura
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.nombre = nombre
    def atacar(self, otro):
        res = otro.vida - int(self.ataque - otro.defensa/4)
        if otro.vida == 0: print("Tu enemigo ya está muerto...")
        elif res < 0:
            el("Eliminaste heroicamente a tu enemigo")
            otro.vida = 0
        elif res >= otro.vida:
            el("Estos ataques ya no surten efecto, solo queda esperar la muerte...")
        else: 
            el(f"Ataque exitoso. Daño: {int(self.ataque - otro.defensa/4)}. Vida de {otro.nombre}: {res}")
            otro.vida = res
        if self._contador_habilidad > 0: self._contador_habilidad -= 1
    @abstractmethod
    def habilidad_especial():
        pass
    def get_estadisticas(self):
        el(f"Nombre: {self.nombre} \nArma: {self.arma} \nArmadura: {self.armadura} \nAtaque: {self.ataque} \nDefensa: {self.defensa} \nVida: {self.vida}")

class Objetos():
    def __init__(self, daño, dureza, nombre):
        self.daño = daño
        self.dureza = dureza
        self.nombre = nombre

class Caballero(Personajes):
    def __init__(self, arma, armadura, ataque, defensa, vida, nombre):
        super().__init__(arma, armadura, ataque, defensa, vida, nombre)
        self._contador = 0
        self._contador_habilidad = 0
        self._habilidad_posible = True
        self._aumentar_defensa_posible = True
    def atacar(self, otro):
        super().atacar(otro)
    def habilidad_especial(self, otro):
        dmg = int(self.ataque + self.ataque/4)
        if self._contador_habilidad == 0:
            res = otro.vida - int(dmg - otro.defensa/4)
            el(f"Habilidad especial: SUPER GOLPE. Realizas un golpe de {res} de daño")
            if otro.vida == 0: el("Tu enemigo ya está muerto...")
            elif res < 0:
                el("Eliminaste heroicamente a tu enemigo")
                otro.vida = 0
            elif res >= otro.vida:
                el("Tu habilidad no surtió efecto. Estas en la peor situación posible, la muerte es inevitable, la mayoría se han quitado su propia vida llegados a este punto...")
            else: otro.vida = res
            el(f"La vida de {otro.nombre} es: {otro.vida}")
            self._contador_habilidad +=3
            self._habilidad_posible = True
        elif self._contador_habilidad > 0: 
            el(f"Tu habilidad especial se está recargando, estará disponible en {self._contador_habilidad} turnos.")
            self._habilidad_posible = False
    def aumentar_defensa(self, batalla):
        if batalla and self._contador == 3:
            el("Ya no puedes aumentar más tu defensa.")
            self._aumentar_defensa_posible = False
        elif batalla:
            self.defensa += 12
            self._contador += 1
            el(f"Tu defensa ha aumentado en 12. Tu nueva defensa es: {self.defensa}")
            if self._contador_habilidad > 0: self._contador_habilidad -= 1
        else:
            self.defensa -= self._contador*12
            self._contador = 0
            self._contador_habilidad = 0
            self._aumentar_defensa_posible = True

class Mago(Personajes):
    def __init__(self, arma, armadura, ataque, defensa, vida, nombre):
        super().__init__(arma, armadura, ataque, defensa, vida, nombre)
        self._contador = 0
        self._contador_habilidad = 0
        self._habilidad_posible = True
        self._aumentar_defensa_posible = True
    def atacar(self, otro):
        super().atacar(otro)
    def habilidad_especial(self, otro):
        dmg = int(self.ataque + self.ataque/4)
        if self._contador_habilidad == 0:
            res = otro.vida - (int(dmg - otro.defensa/4))
            el(f"Habilidad especial: DISPARO RECARGADO. Realizas un disparo de {res} de daño")
            if otro.vida == 0: el("Tu enemigo ya está muerto...")
            elif res < 0:
                el("Eliminaste heroicamente a tu enemigo")
                otro.vida = 0
            elif res >= otro.vida:
                el("Tu habilidad no surtió efecto. Estas en la peor situación posible, la muerte es inevitable, la mayoría se han quitado su propia vida llegados a este punto...")
            else: otro.vida = res
            el(f"La vida de {otro.nombre} es: {otro.vida}")
            self._contador_habilidad += 3
            self._habilidad_posible = True
        elif self._contador_habilidad > 0: 
            el(f"Tu habilidad especial se está recargando, estará disponible en {self._contador_habilidad} turnos.")
            self._habilidad_posible = False
    def aumentar_defensa(self, batalla):
        if batalla and self._contador == 3:
            el("Ya no puedes aumentar más tu defensa.")
            self._aumentar_defensa_posible = False
        elif batalla:
            self.defensa += 12
            self._contador += 1
            el(f"Tu defensa aumentó en 12. Tu nueva defensa es: {self.defensa}")
            if self._contador_habilidad > 0: self._contador_habilidad -= 1
        else:
            self.defensa -= self._contador*12
            self._contador = 0
            self._contador_habilidad = 0
            self._aumentar_defensa_posible = True

class Enanos (Personajes):
    def __init__(self, arma, armadura, ataque, defensa, vida, nombre):
        super().__init__(arma, armadura, ataque, defensa, vida, nombre)
        self._habilidad_posible = True
        self._contador_habilidad = 0
    def habilidad_especial(self, otro):
        dmg = int(self.ataque*1.3)
        if self._contador_habilidad == 0:
            res = otro.vida - (int(dmg - otro.defensa/4))
            el(f"Habilidad especial: TURBO GOLPE ELECTRICO. Realizas un golpe de {res} de daño")
            if otro.vida == 0: el("Tu enemigo ya está muerto...")
            elif res < 0:
                el("Eliminaste heroicamente a tu enemigo")
                otro.vida = 0
            elif res >= otro.vida:
                el("Tu habilidad no surtió efecto. Estas en la peor situación posible, la muerte es inevitable, la mayoría se han quitado su propia vida llegados a este punto...")
            else: otro.vida = res
            el(f"La vida de {otro.nombre} es: {otro.vida}")
            self._contador_habilidad += 3
            self._habilidad_posible = True
        elif self._contador_habilidad > 0: 
            el(f"Tu habilidad especial se está recargando, estará disponible en {self._contador_habilidad} turnos.")
            self._habilidad_posible = False

class Trolls (Personajes):
    def __init__(self, arma, armadura, ataque, defensa, vida, nombre):
        super().__init__(arma, armadura, ataque, defensa, vida, nombre)
        self._habilidad_posible = True
        self._contador_habilidad = 0
    def habilidad_especial(self, otro):
        dmg = int(self.ataque*1.3)
        if self._contador_habilidad == 0:
            res = otro.vida - (int(dmg - otro.defensa/4))
            el(f"Habilidad especial: TERREMOTO INFERNAL. Realizas {res} de daño")
            if otro.vida == 0: el("Tu enemigo ya está muerto...")
            elif res < 0:
                el("Eliminaste heroicamente a tu enemigo")
                otro.vida = 0
            elif res >= otro.vida:
                el("Tu habilidad no surtió efecto. Estas en la peor situación posible, la muerte es inevitable, la mayoría se han quitado su propia vida llegados a este punto...")
            else: otro.vida = res
            el(f"La vida de {otro.nombre} es: {otro.vida}")
            self._contador_habilidad += 3
            self._habilidad_posible = True
        elif self._contador_habilidad > 0: 
            el(f"Tu habilidad especial se está recargando, estará disponible en {self._contador_habilidad} turnos.")
            self._habilidad_posible = False

def el(texto, delay=0.05):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(delay)
    print()

espada1 = Objetos(15, 0, "espada de bronce")
chaleco1 = Objetos(0, 30, "chaleco de cuero")
varita1 = Objetos(27, 0, "varita de tierra")
tunica1 = Objetos(0, 18, "túnica encantada")
espada2 = Objetos(24, 0, "espada de oro")
chaleco2 = Objetos(0, 60, "chaleco de hierro")
varita2 = Objetos(40, 0, "varita de fuego")
tunica2 = Objetos(0, 40, "túnica super encantada")
espada3 = Objetos(45, 0, "espada de diamante")
chaleco3 = Objetos(0, 120, "chaleco de diamante")
varita3 = Objetos(63, 0, "varita de luz")
tunica3 = Objetos(0, 80, "túnica suprema")

caballero = Caballero(espada1.nombre, chaleco1.nombre, int(30 + espada1.daño/3), int(45 + chaleco1.dureza/2), 450, "Sobrino del inframundo")
mago = Mago(varita1.nombre, tunica1.nombre, int(44 + varita1.daño/3), int(12 + tunica1.dureza/2), 360, "Ahijado de dios")

enano = Enanos("Daga", "Ninguna", 45, 14, 105, "enano inexperto")
troll = Trolls("Garrote de madera", "Ninguna", 232, 50, 170, "troll bebe")
enano1 = Enanos("Machete", "chaleco de malla", 72, 25, 220, "enano guardian")
troll1 = Trolls("Garrote con clavos", "Ninguna", 56, 80, 280, "troll guardian")
enano2 = Enanos("Brazos mecánicos", "Medio cuerpo metálico", 125, 60, 500, "señor de las cavernas")
troll2 = Trolls("Hacha celestial", "Armadura completa de hierro", 85, 140, 620, "heredero de la tierra")