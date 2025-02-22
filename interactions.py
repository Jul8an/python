import main as mn
import time
import random

juego = True

def escribir_lento(texto, delay=0.05):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(delay)
    print()

escribir_lento("Bienvenido valiente viajero... Este es el cominezo de tu fin... ¿O no?")

while True:
    user = input("¿Qué personaje quieres usar: caballero o mago? ")
    if user == "mago" or user == "Mago":
        user = mn.mago
        break
    elif user == "caballero" or user == "Caballero":
        user = mn.caballero
        break
    else: print("Por favor, inserte un personaje válido")

escribir_lento("Esto es lo que necesitas saber sobre ti:")
user.get_estadisticas()

time.sleep(1.5)

escribir_lento("Ahora que has elegido tu camino... Tu aventura comenzará.")
escribir_lento("Vives en una aldea bastante traquila, llamativamente tranquila dirían algunos, pero solamente llamativa para aquellos que no la habitan. Quienens viven aquí, disfrutan de la paz, presuntamente otorgada por los dioses.")
escribir_lento(f"Tú eres perspicaz, sabes bien que no es así, y aún así no te preocupa, aceptas que hay cosas que están fuera de tu comprensión y ya. No te gusta tanto esta paz. La paz que todos en el mundo anhelan, no es de tu agrado. \nTu espíritu pide más acción. Eres un viajero innato. Ahora que estas en edad, y ya has elegido tu profesión, tú, {user.nombre}, emprenderás un viaje...")
time.sleep(1)
escribir_lento("Antes de partir, haces la investigación correspondiente, y ningún lugar parece apropiado para tu primera aventura. Quieres algo tranquilo, por ser la primera vez.")
escribir_lento("Nada parece prometedor, excepto por un lugar. Hay una cueva en las afueras de tu pueblo, más cerca de lo que a cualquiera le gustaría. No está iluminada, por lo que no se ve el final. No encontraste nada sobre ella en ningún lado, debe ser porque es tan pequeña que no vale la pena documentarla.")
escribir_lento("Preparativos listos, y sin saludar a nadie, te vas. No saludas porque esperas volver como mucho al día siguiente... Maldito iluso.")
escribir_lento("Entras en la cueva, prendes la antorcha, y comienzas a caminar. El camino esta demasiado derecho. Te llama la atención, pero, ¿Qué puedes hacer? Sigues caminando, y caminando, y caminando, durante más de 40 minutos.")
escribir_lento("Al parecer la cueva no era tan pequeña, te ilusionas con ser el primero en dejar registro sobre ella.")
time.sleep(1)
escribir_lento("Mayor fue tu ilusión y tu sorpresa, cuando encuentras una extraña bifurcación. Perfectamente marcada. Dos caminos que llevan en direcciones opuestas. Quien sabe a cuantos metros bajo tierra estas en este punto, o lo extraño de tu hallazgo. \nTú quieres seguir, y te ves en la obligación de decidir...")

while True:
    camino = input("¿Qué camino eliges: derecha o izquierda? ")
    enemigo = None
    if camino == "derecha" or camino == "Derecha":
        enemigo = mn.Enanos("Daga", "Ninguna", 40, 14, 105, "enano inexperto")
        enemigo1 = mn.Enanos("Daga", "Ninguna", 40, 14, 105, "enano inexperto")
        enemigo2 = mn.Enanos("Daga", "Ninguna", 40, 14, 105, "enano inexperto")
        break
    elif camino == "izquierda" or camino == "Izquierda":
        enemigo = mn.Trolls("Garrote de madera", "Ninguna", 27, 50, 170, "troll bebe")
        enemigo1 = mn.Trolls("Garrote de madera", "Ninguna", 27, 50, 170, "troll bebe")
        enemigo2 = mn.Trolls("Garrote de madera", "Ninguna", 27, 50, 170, "troll bebe")
        break
    else: print("Por favor, elige uno de los dos caminos.")

escribir_lento(f"Has elegido ir por la {camino} y muy pronto te preguntas si no cometiste un error fatal, ya que pocos minutos de caminata después te encuentras a un {enemigo.nombre}!!!")
time.sleep(1)
escribir_lento("No tienes otra opción más que luchar...")
enemigo.get_estadisticas()

while True:
    while True:
        accion = input("¿Qué deseas hacer? \nAtacar (1) \nAumentar tu defensa (2) \nUsar habilidad especial (3) \n")
        if accion == "1": 
            user.atacar(enemigo) 
            break
        elif accion == "2": 
            user.aumentar_defensa(True)
            if user._aumentar_defensa_posible == True: break
            elif user._aumentar_defensa_posible == False: continue
        elif accion == "3":
            user.habilidad_especial(enemigo)
            if user._habilidad_posible == True: break
            elif user._habilidad_posible == False: continue
        else: escribir_lento("Por favor, elige una opción válida")
    if enemigo.vida == 0: break
    print(f"El {enemigo.nombre} contraataca")
    enemigo.atacar(user)
    if user.vida == 0: 
        escribir_lento("Es triste pero, tu aventura llegó a su fin... Hasta nunca viajero.")
        juego = False
        break
user.aumentar_defensa(False)

if juego == False: exit()

escribir_lento("Fue una dura batalla...")
escribir_lento("Ni siquiera esperabas tener que luchar, solo querías explorar la mazmorra en busca de minerales. Podría llegar a haber alguna que otra bestia, pero esto...")
escribir_lento(f"Encontrarse un {enemigo.nombre} no es normal, es obvio que hay algo que no te has enterado. A estas alturas, no sabes si es mejor volver o seguir un poco más.")
time.sleep(2)
escribir_lento("Decides seguir...")
time.sleep(0.5)
escribir_lento("Ahora te encuentras a toda una familia de criaturas!!")
escribir_lento(f"Era evidente que el {enemigo.nombre} a quien mataste no estaba solo, pero esto no está bien. Estas criaturas no suelen vivir tantos metros bajo tierra.")
escribir_lento("¿Cuál será su motivo? ¿Cómo pueden vivir aquí? ¿Qué los mantiene en esta mazmorra? ¿Recursos? ¿Tesoros? ¿Alguien los esclavizó?")
escribir_lento("Ahora no es tiempo de responder estás preguntas. Dos de ellos deciden hacerte frente. No tienen oportunidad, pero ellos nos lo saben... Toca ensuciarse las manos.")

while True:
    while True:
        accion = input("¿Qué deseas hacer? \nAtacar (1) \nAumentar tu defensa (2) \nUsar habilidad especial (3) \n")
        if accion == "1": 
            if enemigo1.vida != 0:
                user.atacar(enemigo1)
                user.atacar(enemigo2)
                break
            else: 
                user.atacar(enemigo2)
                break
        elif accion == "2": 
            user.aumentar_defensa(True)
            if user._aumentar_defensa_posible == True: break
            elif user._aumentar_defensa_posible == False: continue
        elif accion == "3":
            if enemigo1.vida != 0: user.habilidad_especial(enemigo1)
            else: user.habilidad_especial(enemigo2)
            if user._habilidad_posible == True: break
            elif user._habilidad_posible == False: continue
        else: escribir_lento("Por favor, elige una opción válida")
    if enemigo1.vida == 0 and enemigo2.vida == 0: break
    elif enemigo1.vida != 0 and enemigo2.vida != 0:
        print("Ambos contra atacan")
        enemigo1.atacar(user)
        enemigo2.atacar(user)
    elif enemigo1.vida == 0 and enemigo2.vida != 0:
        print("El enemigo contrataca")
        enemigo2.atacar(user)
    if user.vida == 0: 
        escribir_lento("Es triste pero, tu aventura llegó a su fin... Hasta nunca viajero.")
        juego = False
        break
user.aumentar_defensa(False)
if juego == False: exit()



escribir_lento("Miras tu reflejo en tus manos manchadas de sangre...")
time.sleep(0.5)
escribir_lento("Nunca has hecho esto antes, sin embargo, sabes que es un precio a pagar por ser viajero en este mundo tan hostil. Creías que siempre tendrías una razón para hacerlo, que no serías como los demás viajeros que desprecias. \n Aquellos que viajan y roban todo lo que pueden, y asesinan a quien se les cruza. Tú no querías eso. Estabas dispuesto a hacerlo, pero no lo querías.")
escribir_lento("Es la paradoja del viajero que intenta ser buena persona. Tú ibas a luchar contra ella. Pensabas que matar en defensa popia si estaba permitido, porque es necesario.")
escribir_lento("Ahora, te sientes diferente, sientes que el extraño eres tú, que el invasor eres tú, y ellos solo están intentando defender lo que es suyo ante una amenaza desconocida.")
escribir_lento("Sí, mataste en defensa propia. De la misma manera que mataría un ladrón a quienes viven dentro de una casa que él mismo quiso robar, alegando que su vida corría peligro. Todos saben de qué lado estaría el juez de la moral")
time.sleep(0.5)
escribir_lento("Sigues avanzando, cargando con tu pesar, a sabiendas de que tu retirada, a este punto, podría poner a tu aldea en peligro de sufrir una guerra contra un poder desconocido. Porque así como encontraste una familia, debe haber más. Debes, al menos, ser consciente de a qué se enfrentarían antes de retirarte.")
escribir_lento("Sin darte cuenta, estuviste más de una hora reflexionando, hasta que al fin te dignaste a retomar tu camino. \nLa mazmorra parece no tener final. Luego de 30 minutos de andar, encuentras una aldea, la primera de muchas, seguramente, pero está vacía...")
time.sleep(0.3)
escribir_lento("A partir de aquí encuentras una atrás de otra, todas vacías. Es claro que saben de tu presencia. Estás a punto de emprender el regreso, creyendo haber visto suficiente como para alertar a tu aldea de que es hora de mudarse, hasta que ves unas escaleras gigantes...")
escribir_lento("¿Cómo? ¿Cuándo? ¿Por qué? ¿Por qué nadie tiene registro sobre esto? ¿Es que nadie que haya llegado tan lejos sobrevivió para contarlo? Definitivamente no tienes idea de a qué te enfrentas... Definitivamente.")
escribir_lento("Ya no sabes si es seguro escapar. Se necesita demasiada fuerza y maquinaria para construir lo que estas presenciando. No sabes si tu aldea escaparía a tiempo, o si tú lo harás...")
escribir_lento("<<<A veces, la mejor defensa es un buen ataque>>> Es lo primero que se te viene a la mente.")
time.sleep(1)
escribir_lento("Te retractas de tu pensamiento. El camino del diálogo es el adecuado. Si alguien es tan inteligente y capaz para construir esto, tal vez también lo sea para dialogar. 3 largas horas pasaron, y tu aventura continúa...")
time.sleep(1)
escribir_lento("NIVEL 1 COMPLETADO \nENTRANDO AL NIVEL 2... ")
time.sleep(3)
escribir_lento("SUBES DE NIVEL!!!")
if user == mn.mago:
    user.vida += 50
    user.ataque += 15
    user.defensa += 10
elif user == mn.caballero:
    user.vida += 100
    user.ataque += 8
    user.defensa += 20
escribir_lento(f"Estas son tus nuevas estadísticas:")
user.get_estadisticas()

escribir_lento("Antes de bajar por las escaleras, revisas algunas casas en busca de armamento, o tal vez un plato de comida listo, para poder guardar tus provisiones para más tarde")
escribir_lento("En la primera casa que entras ves un plato de sopa frío servido en la mesa. Lo aprovechas. Es más digno comerlo que tirarlo, honrando la cena que ya le arruinaste a alguien más.")
escribir_lento("Te levantas sin hacer sobre mesa, y sigues revisando casas, una atrás de la otra, y ninguna tiene armas o armaduras. Claramente es una aldea pacífica, la cual no tiene esas cosas al no sentir necesidad. De ahora en más, quizás empiecen a tenerlas, quien sabe...")
escribir_lento("Cansado de buscar, decides probar otro enfoque. Usas la vista, prestas más atención a tu alrededor. Seguramente haya algo que te de una pista. Al menos uno debe ser un guerrero. Y tenías razón, uno lo es. \nLa casa más alta de todas, tiene una chimenea con diseño de espada, y un escudo en la parte superior de la puerta. Entras y notas que es más espaciosa que las demás, y un poco diferente, como que no la habita una familia.")
escribir_lento("Subes al segundo piso y encuentras lo que parece ser una oficina, con dos cofres enormes. Bingo. Esta tiene que ser la casa del jefe de la aldea. Y debe tener algo bueno...")

while True:
    if user == mn.mago:
        escribir_lento("Has encontrado una varita y una túnica, pero solo puedes llevar una.")
        opcion = input("¿Cuál eliges?").lower()
        if opcion == "varita":
            user.arma = mn.varita2.nombre
            user.ataque += int(mn.varita2.daño/3)
            escribir_lento(f"¡Has conseguido una nueva varita! Ahora tienes una {user.arma} y tu nuevo ataque es {user.ataque}.")
            break
        elif opcion == "tunica":
            user.armadura = mn.tunica2.nombre
            user.defensa += int(mn.tunica2.dureza/2)
            escribir_lento(f"¡Has conseguido una nueva túnica! Ahora tienes una {user.armadura} y tu nueva defensa es {user.defensa}.")
            break
        else: print("Por favor, elige una de las dos opciones.")
    elif user == mn.caballero:
        escribir_lento("Has encontrado una espada y un chaleco, pero solo puedes llevar una.")
        opcion = input("¿Cuál eliges?").lower()
        if opcion == "espada":
            user.arma = mn.espada2.nombre
            user.ataque += int(mn.espada2.daño/3)
            escribir_lento(f"¡Has conseguido una nueva espada! Ahora tienes una {user.arma} y tu nuevo ataque es {user.ataque}.")
            break
        elif opcion == "chaleco":
            user.armadura = mn.chaleco2.nombre
            user.defensa += int(mn.chaleco2.dureza/2)
            escribir_lento(f"¡Has conseguido un nuevo chaleco! Ahora tienes un {user.armadura} y tu nueva defensa es {user.defensa}.")
            break
        else: print("Por favor, elige una de las dos opciones.")

escribir_lento("Ahora sí estás listo para bajar. Sales cuidadosamente de la casa, y te diriges hacia las escaleras. \nEstá todo bien iluminado, y hay claros indicios de qué muchas personas las usaron recientemente.")
escribir_lento("Algunos envoltorios tirados, servilletas, en fin, basura, acompañada de muchas huellas. Es dificil mantener la limpieza tantos metros bajo tierra, por eso será que quedan tan marcadas las pisadas.")
escribir_lento("Escuchas el eco de tus zapatos durante todo tu andar, el cual no duró mucho. A pesar de ser tan grande la escalera, no era muy larga. Y como ya te imaginabas, una aldea emerge al pie de la misma, y como también te imaginabas, te estaban esperando...")
escribir_lento("Esta vez, no era poca cosa. Lo que tenías en frente, posiblemente explicaba por qué nadie pudo registrar todo lo que estabas viendo. Estaba solo, confiado. Tu vida corre peligro, esta vez de verdad.")

if enemigo.nombre == "enano inexperto":
    enemigo3 = mn.Enanos("Machete", "chaleco de malla", 67, 25, 220, "enano guardian")
    enemigo4 = mn.Enanos("Machete", "chaleco de malla", 67, 25, 220, "enano guardian")
    enemigo5 = mn.Enanos("Machete", "chaleco de malla", 67, 25, 220, "enano guardian")
elif enemigo.nombre == "troll bebe":
    enemigo3 = mn.Trolls("Garrote con clavos", "Ninguna", 51, 80, 280, "troll guardian")
    enemigo4 = mn.Trolls("Garrote con clavos", "Ninguna", 51, 80, 280, "troll guardian")
    enemigo5 = mn.Trolls("Garrote con clavos", "Ninguna", 51, 80, 280, "troll guardian")

time.sleep(1)
escribir_lento(f"Te enfrentas a un {enemigo3.nombre}...")
enemigo3.get_estadisticas()
time.sleep(1)

while True:
    while True:
        accion = input("¿Qué deseas hacer? \nAtacar (1) \nAumentar tu defensa (2) \nUsar habilidad especial (3) \n")
        if accion == "1": 
            user.atacar(enemigo3) 
            break
        elif accion == "2": 
            user.aumentar_defensa(True)
            if user._aumentar_defensa_posible == True: break
            elif user._aumentar_defensa_posible == False: continue
        elif accion == "3":
            user.habilidad_especial(enemigo3)
            if user._habilidad_posible == True: break
            elif user._habilidad_posible == False: continue
        else: escribir_lento("Por favor, elige una opción válida")
    if enemigo3.vida == 0: break
    print(f"El {enemigo3.nombre} contraataca")
    enemigo3.atacar(user)
    if user.vida == 0: 
        escribir_lento("Es triste pero, tu aventura llegó a su fin... Hasta nunca viajero.")
        juego = False
        break
user.aumentar_defensa(False)

if juego == False: exit()

escribir_lento("Este maldito sí que te hizo sufrir. Estas lastimado, sangrando, sientes un poco de frío y todo tu cuerpo duro. Solo quieres descanar, pero no es seguro. Al menos debes esconderte en alguna casa.")
escribir_lento("Entras a la primera que ves a tu derecha. Estas casas no se parecen en nada a las que modelaban el paisaje de la cueva en el piso de arriba. \n´Debe ser que me estoy acercando de a poco al núcleo de todo esto, y de la misma manera que nos organizamos los humanos, las ciudades del centro son más ricas que las aldeas de las periferias´")
escribir_lento("Te recuestas en el sillón de la sala, y tu hemorragia comienza a detenerse. No era la gran cosas después de todo. Tapado con el mantel de la mesa, los ojos se te empiezan a cerrar, pero no es momento de descansar viajero...")
escribir_lento("Mientras te encuentras en el limbo entre estar dormido y despierto, un repentino ruido de saca de él. Escuchas pasos, graves, y una voz que lo es aún más. No entiendes lo que dice, pero reconoces su intención.")
escribir_lento(f"Te das cuenta de que se está acercando otro {enemigo3.nombre} a ver el resultado de la batalla. ´Sería genial tener la habilidad de imitar voces para decirle que está todo bien, y aprovechar para escapar´ piensas. Ante la duda, te escondes detrás de la mesada que separa la cocina y el comedor, para que no te vean por la ventana.")
escribir_lento("Los pasos se escuchan cada vez más fuerte, cada vez más cerca, hasta que se detienen. Sin un poco de tristeza en la voz, escuchas el grito más escalofriante de tu vida, y lo peor es que no estaba tratando de asustar a nadie, sino solo llamar a su compañero.")
escribir_lento(f"Es entonces cuando ves a otro {enemigo3.nombre} acercarse a analizar la situación. Deseabas que no hubiese más de esas criaturas, pero muy en el fondo sabías que era un deseo inútil, una esperanza sin sentido a la que no te aferraste para no decepcionarte en vano.")
escribir_lento("A estas alturas, el sueño se te había ido por completo. La adrenalina te inundaba. No sabíás si era por miedo o por la democión de la aventura que estabas viviendo. A tu parecer, tenías dos opciones: o ese era el último día de tu vida, o si salías vivo de ahí, serías el mejor aventurero de todos los tiempos. Era todo o nada. Lo que, en principio, era una simple exploración para empezar a ganar experiencia, se convirtió en el mayor punto de inflexión de tu vida.")
escribir_lento("De pronto, los guardias, de los que te habías olvidado por un momento, disparan algo hacia el techo de la cueva. Más bien, simplemente hacia arrriba, porque el techo debía estar 100 metros hacia arriba cuanto menos. No llegas a ver bien qué pasa, pero ves a través de la ventana que el panorama se vuelve rojizo por un momento, y luego vuelve a la normalidad.")
escribir_lento("´Dieron una señal, pero ¿de qué? No harían tanto escándalo solo para avisar que su compañero murió, ¿o sí?´ De un momento a otro, los guardias comienzan a correr en dirección opuesta a la escalera, y medio segundo después, un estruendo te estremece el cuerpo al punto de marearte brevemente. Recuperas la compostura a los pocos segundos para descubrir que el sonido sigue ahí, pero a muchos decibeles menos.")
escribir_lento("´Una bomba no fue, porque no seguiría sonando. ¿Qué demonios puede hacer semejante ruido durante tanto tiempo seguido?´ Un objeto enorme en movimiento sería capaz de semejante ruido, pero aún no has llegado a esa conclusión. Con mucho cuidado, te recompones y sales de la casa.")
escribir_lento("Primero, hechas  un vistazo hacia el lado que se fueron los guardias, no vaya a ser que te esten esperando. Luego de convencerte de que no están ahí, te das vuelta, solo para ver un pedazo de hierro enorme sellando rapidamente la salida de arriba hacia abajo...")
escribir_lento("Un escalofrío recorre tu cuerpo, y corres hacia la escalera a toda velocidad con la esperanza de llegar antes de que se selle completamente tu única salida.")
time.sleep(1)
escribir_lento("Esta vez sí te dejaste consumir por una falsa esperanza...")
time.sleep(1)
escribir_lento("La puerta se cerró en tu cara y fue tal el estruendo y el choque contra el piso que saliste volando hacia atrás, aturdido nuevamente. Miras al techo. Recuerdas una frase que leiste: ´Cuando rodees a tu enemigo, deja siempre una salida libre´. ´Estos imbeciles cometieron un error al encerrarme acá abajo´ El miedo y la duda desapaecen. De a poco, te pones de pie. Tu cara irradia esa decisión que ahora sientes por dentro. La batalla de verdad ha comenzado.")
escribir_lento("Solo tienes una opción: encontrar a quienes te cerraron la puerta, matarlos a todos, abrirla, e irte a tu casa. Esa compasión que habías sentido en un principio, se había ido. Tus ganas de dialogar, también. Estás eufórico. Y comienzas a caminar, buscando al responsable de todo esto.")
escribir_lento("Vas caminando por lo que parece ser la avenida principal. Ya no te importa si te ven. Sigues esta calle con la esperanza de que te lleve a algo. Y así lo fue. Después de haber caminado durante una hora, sin ningún imprevisto, llegas a una especie de plaza central. En el medio de la misma, hay una construcción bastante grande, que no se molesta en ocultar que es ayuntamiento de la ciudad.")
escribir_lento("Entras, un poco por curiosidad, otro poco con la intención de encontrar algo que te sirva. El recinto es tan grande que te hace plantearte cuanto tiempo estas dispuesto a dedicar a revisarlo. Solo el hall es más grande que tu casa. Te vas directamente en busca de la oficina del cabecilla.")
escribir_lento("No fue facil encontrarla, todas las oficinas se ven bastante parecidas. La única diferencia entre la que buscabas y las demás es la silla. Debe ser por algún tema de estatus o algo. Una vez dentro, ya encuentras más diferencias. El material de los muebles, el grosor de los candados que guardan las cosas en unos casilleros, y uno que otro plano de la ciudad que no habías visto en los otros lugares.")
escribir_lento("Observas atentamente los planos, y notas que no hay solo de esta ciudad, sino de algunas vecinas, y lo que parecer ser un plano general de este ´piso´ de la cueva. Esta todo demasiado bien organizado y ordenado, a partir del mapa resulta claro que la construcción del piso entero de planeó con antelación.")
escribir_lento("´¿Quién o quiénes pudieron planear todo esto y luego construirlo?´ tampoco te importa mucho a esta altura, pero te da una idea de lo que se viene. El plano era simple, mostraba la distribución de las ciudades y sus principales características, y todas estaban construidas alrededor de un círculo en el medio, que no tenía ninguna referencia ni detalle ni nada. ´Mi objetivo será llegar ahí entonces´.")
escribir_lento("Sobre la ciudad en la que te encuentras, dice que la inseguridad es muy baja y se destacan por la manufacturación de zapatos. Tuviste suerte de entrar por la cueva que lo hiciste. Quien sabe cuantas entradas tendrá esta comunidad en un radio de varios kilómetros.")
escribir_lento("Cierras el mapa y lo guardas en tu bolsa de viaje. Revisas toda la habitación antes de irte, y encuentras unas botellas de vidrio pequeñas, con un líquido rojo en su interior. Ante la imposibilidad de abrir esos casilleros, esto es lo mejor que tienes. Te da bronca porque piensas que debe ser lo que no entraba en los casilleros ni tampoco se pudieron llevar y lo descartaron. Aún así, lo guardas, y retomas tu camino.")
time.sleep(2)
escribir_lento("El mapa no marcaba muy bien las distancias, pero sí tenía fijado con un punto los distintos ayuntamientos de cada ciudad, por lo que, tomando como referencia donde estabas, masomenos te haces una idea de cuanto viaje te queda hasta el centro.")
escribir_lento("´A juzgar por lo que ví, la ciudad debe tener unos 5 kilómetros de largo, desde la escalera al centro. Debo apresurarme antes de que vengan a emboscarme. A veces un buen ataque es la mejor defensa´")
escribir_lento("En el camino al círculo misterioso del centro de este piso, pasas por al lado de lo que parece ser una tienda, bastante más colorida que las demás. Esta lleno de cofres aburridos irrompibles como los del ayuntamiento, pero en las paredes ves unos carteles con precios y referencias. Miras un poco hacia arriba, y ves un letrero enorme encima de la ventana por la que atienden que dice ´TIENDA DE POCIONES´")
escribir_lento("Te acercas a ver las referencias, y ves que el color rojo dice ´poción de vida´. Bingo. En tu mochila tienes 3 pequeñas pociones de vida. No vienen envasadas de la misma manera que en la superficie, podían ser cualquier cosa, pero acá abajo, deben ser, solo hay una forma de saberlo.")
escribir_lento("Te tomas una y...")
time.sleep(2)
user.vida += 140
escribir_lento(f"¡Qué suerte tienes! ¡Ahora te sientes mucho mejor, era una poción de vida! Tu nueva vida es {user.vida}. Decides guardarte las otras dos por las dudas. Si no estabas del todo confiado, ahora lo estás. No solo tienes tus increibles habilidades, ahora también tienes vida extra.")
escribir_lento("Mientras sigues avanzando, escuchas a lo lejos una caravana. Distingues algunos caballos, voces, armas, y ya no quieres seguir perdiendo el tiempo en eso porque ya entendiste el mensaje. Están viniendo por tí.")
escribir_lento("Aceleras el paso, más bien, comienzas a correr. A medida que avanzas, comienzas a escuchar un sonido familiar: fluye agua. En algún lugar, a tantos metros bajo tierra, fluye agua. Mucha agua. 5 minutos después y estabas parado frente a un árbol gigante. Esa era la figura alrededor de la que se construyeron todas las ciudades. El árbol es tan grande que aún mirando para los costados no llegas a a ver su curvatura.")
escribir_lento("Hacia arriba, su altura penetra el techo, y ves como alrededor de él están construidas unas canaletas que guían un río de agua dulce que nace de una de las paredes. El río gira en torno al tronco para perderse bajo el piso con él. Las raíces del arbol están más abajo, esperemos que en lo que sea el último piso.")
escribir_lento("La avenida por la que venías corriendo se choca con una puerta que da hacia adentro del árbol. ´Debe ser que ahí hay un asensor o algo para bajar´. Debes entrar a averiguarlo, pero custodiando la puerta, están los dos guardias que habías escuchado más temprano.")
escribir_lento("Es tu momento de luchar, son ellos o la multitud que escuchaste más atras. Debes ser rápido, antes de que te alcancen.")
escribir_lento("Haces una pausa, te tomas las otras dos pociones de vida, sabiendo que dentro del arbol deben tener más. Es decir, es un puesto de guardia. Por lo general, allí se guardan algunos suministros para los guardias de turno.")
user.vida += 140*2
time.sleep(.5)
escribir_lento("Arremetes contra ellos sin ningún sigilo, intentando aún así sorprenderlos, e increiblemente funciona. Les asestas un buen churrazo a cada uno y tomas distancia. Sufrieron el daño, definitivamente, pero rapidamente se recomponen, y están listos para acabar contigo...")
escribir_lento("La vida de tus enemigos se redujo en 30 gracias a tu astucia y valentía.")
enemigo4.vida -= 30
enemigo5.vida -= 30
while True:
    while True:
        accion = input("¿Qué deseas hacer? \nAtacar (1) \nAumentar tu defensa (2) \nUsar habilidad especial (3) \n")
        if accion == "1": 
            if enemigo4.vida != 0:
                user.atacar(enemigo4)
                user.atacar(enemigo5)
                break
            else: 
                user.atacar(enemigo5)
                break
        elif accion == "2": 
            user.aumentar_defensa(True)
            if user._aumentar_defensa_posible == True: break
            elif user._aumentar_defensa_posible == False: continue
        elif accion == "3":
            if enemigo4.vida != 0: user.habilidad_especial(enemigo4)
            else: user.habilidad_especial(enemigo5)
            if user._habilidad_posible == True: break
            elif user._habilidad_posible == False: continue
        else: escribir_lento("Por favor, elige una opción válida")
    if enemigo4.vida == 0 and enemigo5.vida == 0: break
    elif enemigo4.vida != 0 and enemigo5.vida != 0:
        print("Ambos contra atacan")
        enemigo4.atacar(user)
        enemigo5.atacar(user)
    elif enemigo4.vida == 0 and enemigo5.vida != 0:
        print("El enemigo contrataca")
        enemigo5.atacar(user)
    if user.vida == 0: 
        escribir_lento("Es triste pero, tu aventura llegó a su fin... Hasta nunca viajero.")
        juego = False
        break
user.aumentar_defensa(False)
if juego == False: exit()

escribir_lento("Luego de tremenda batalla, no tienes tiempo ni de mirar tus heridas. ´Una poción bastará´ piensas, sin bajar la vista a ver el charco de sangre debajo tuyo. Ya escuchas a la multitud revisando la ciudad, en poco tiempo estarán contigo. Entras al arbol, y del otro lado de la puerta ves lo que hay en todo puesto de control.")
escribir_lento("Armas, armaduras, comida, algunas pociones, mapas, etc. Revisas bien, aunque sabes que no tienes mucho tiempo, pero quieres encontrar algo que te sirva, debe haber. No tienes tiempo de probarte a ver si te quedarían cómodas las ropas, ni tampoco si las armas se ajustan a tu mano.")
escribir_lento("Y a veces, un peor arma pero cómoda, tiene un mayor efecto. Buscas a ver si hay algo que reconozcas. Sales de tu mini trance cuando escuchas a alguien afuera, y luego llega otro, y otro. Encontraron los cuerpos...")
escribir_lento("Tienes solo segundos para irte de ahí. Vas y guardas algunas pociones de vida, primero lo primero. Una chica y una más grande, probablemente de tamaño mediano. Inmediatamente después, te vuelves a las armaduras, antes de bajar por el asensor que se hunde en las entrañas del arbol. Justo a tiempo, reconoces dos elementos de tu talla: arma y armadura. Los agarras, y subes al asensor al mismo tiempo que un guardia abre la puerta.")
escribir_lento("Se miran a los ojos, y el asensor comienza a bajar...")
time.sleep(2)
escribir_lento("SUBES DE NIVEL!!!")
if user == mn.mago:
    user.vida += 80
    user.ataque += 30
    user.defensa += 15
elif user == mn.caballero:
    user.vida += 130
    user.ataque += 16
    user.defensa += 30
if user == mn.mago:
    escribir_lento("Has encontrado una varita y una túnica.")
    if user.arma == mn.varita2.nombre:
        user.arma = mn.varita3.nombre
        user.ataque += int(mn.varita3.daño/3)
        user.armadura = mn.tunica2.nombre
        user.defensa += int(mn.tunica2.dureza/2)
        escribir_lento(f"¡Has conseguido una nueva varita y una nueva túnica! Ahora tienes una {user.arma} y una {user.armadura} y tus nuevos ataque y defensa son {user.ataque} y {user.defensa} respectivamente.")
    elif user.armadura == mn.tunica2.nombre:
        user.armadura = mn.tunica3.nombre
        user.defensa += int(mn.tunica3/2)
        user.arma = mn.varita3.nombre
        user.ataque += int(mn.varita3.daño/3)
        escribir_lento(f"¡Has conseguido una nueva túnica y una nueva varita! Ahora tienes una {user.arma} y una {user.armadura} y tus nuevos defensa y ataque son {user.defensa} y {user.ataque} respectivamente.")
elif user == mn.caballero:
    if user.arma == mn.espada2.nombre:
        user.arma = mn.espada3.nombre
        user.ataque += int(mn.espada3.daño/3)
        user.armadura = mn.chaleco2.nombre
        user.defensa += int(mn.chaleco2.dureza/2)
        escribir_lento(f"¡Has conseguido una nueva espada y un nuevo chaleco! Ahora tienes una {user.arma} y un {user.armadura} y tus nuevos ataque y defensa son {user.ataque} y {user.defensa} respectivamente.")
    elif user.armadura == mn.chaleco2.nombre:
        user.armadura = mn.chaleco3.nombre
        user.defensa += int(mn.chaleco3.dureza/2)
        user.arma = mn.espada2.nombre
        user.ataque += int(mn.espada2.daño/3)
        escribir_lento(f"¡Has conseguido un nuevo chaleco y una nueva espada! Ahora tienes un {user.arma} y una {user.armadura} y tus nuevos defensa y ataque son {user.defensa} y {user.ataque} respectivamente.")

escribir_lento(f"Estas son tus nuevas estadísticas:")
user.get_estadisticas()
time.sleep(2)
escribir_lento("NIVEL 2 COMPLETADO \nENTRANDO AL NIVEL 3...")
time.sleep(1)

escribir_lento("Después de muchas horas, al fin tienes un momento de paz. Sientes que te baja un cansancio desde la cabeza a las piernas, al punto de sentir la imeriosa necesidad de sentarte.")
escribir_lento("En el piso, empiezas a pensar en tu familia, tus amigos y no tan amigos, y otros conocidos de la aldea. Recuerdas el calor de la tierra bajo tus pies esos días de entrenamiento. ´como me dolían las plantas de los pies al terminar cada sesión´.")
escribir_lento("Sientes un poco de nostalgia, mientras el asensor sigue su recorrido. Recuerdas esas noches donde te quedabas mirando las estrellas e imaginando lo que te depara en el mundo. Aventuras, tesoros, gente, historias, tal vez amor...")
escribir_lento("Te pierdes en tus pensamientos, mientras inhalas y exhalas profundamente. Al cabo de unos minutos, sientes que te chocas contra el piso. Tan de golpe frenó el asensor que te asusta, pero solo un poco, de la misma manera que nos asustamos cuando alguien rompe un vaso o explota un globo cerca nuestro, casi que no lo llamamos miedo, es solo un susto.")
escribir_lento("Ese pequeño susto basta para traerte de vuelta a la realidad, te recuerda donde estás y a que viniste. Te pones de pie, sin poder ver nada del otro lado de la puerta del asensor. Mientras esta se abre, te pones en guardia, solo para ver que del otro lado te esperaba una emboscada digna de un cuadro hecho por los mejores artistas. Había guardias por montones, haciendo un semicirculo al frente de la puerta del asensor a un radio de unos 50 metros.")
escribir_lento("No hay que ser muy inteligente para darse cuenta que estás en graves problemas. Empiezas a buscar cuidadosamente con la mirada una abertura para escapar. En eso distingues una impresionante ciudad detrás de todos estos guardias. Construcciones y monumentos equiparables a los de las más grandes ciudades que hay sobre la tierra. A lo lejos, hasta se distingue un castillo.")
escribir_lento("La corriente de agua que bajaba alrededor del arbol, la vez pasando cerca del techo, por un puente hecho solo para ella, y desembocando en el castillo, para luego ramificarse por la ciudad. EL sonido del agua fluyendo, sumado a una correcta y suave iluminación, le daban al lugar un aspecto mucho más agradable del que uno esperaría encontras cientos de metros bajo tierra.")
escribir_lento("Las casas no destacaban por ser precarias sino al contrario, y cuanto más cerca de castillo estaban, más lujosas eran. Quedaste brevemente maaravillado por lo que estaba ante tus ojos, olvidandote por completo de qué era lo que estabas buscando.")
escribir_lento("El semicírculo de guardias se abre en frente tuyo. No estaban arremetiendo para matarte y tampoco parecían querer hacerlo, parecía más bien que esperaban algo.")
escribir_lento("´Tal vez están esperando que yo haga mi movimiento´. No, no esperaban eso. Unos segundos después lo comprendiste, no esperaban algo, sino a alguien...")
time.sleep(1)
escribir_lento("Lo que apareció caminando por ahí, fue tan ridículo que en vez de sentir miedo, te reiste en voz baja y te preguntaste como carajos hizo para esconderse.")
escribir_lento("Tenía mínimo unos 4 metros de alto, y no se lo veía muy amistoso. Se acercó lentamente al centro del semicírculo, y te invitó a acercarte. No de manera amistosa, estaba claramente invitandote a pelear. Ni modo, no tenías opción. Aunque sea una locura, vas a intentarlo. No, mejor dicho, vas a hacerlo, porque así es como nacen las leyendas.")
escribir_lento("Te sacas tu mochila, y te tomas las pociones. Ni siquiera intentó interrumpirte. No porque piense que no hacía falta, no te estaba subestimando, sino porque su ogullo de guerrero no se lo permitió. \nAhora sí, a pelear...")
if enemigo5.nombre == "troll guardian": enemigo6 = mn.Trolls("Hacha celestial", "Armadura completa de hierro", 80, 140, 620, "heredero de la tierra")
elif enemigo5.nombre == "enano guardian": enemigo6 = mn.Enanos("Brazos mecánicos", "Medio cuerpo metálico", 120, 60, 500, "señor de las cavernas")
user.vida += 140 + 280
enemigo6.get_estadisticas()
while True:
    while True:
        accion = input("¿Qué deseas hacer? \nAtacar (1) \nAumentar tu defensa (2) \nUsar habilidad especial (3) \n")
        if accion == "1": 
            user.atacar(enemigo6) 
            break
        elif accion == "2": 
            user.aumentar_defensa(True)
            if user._aumentar_defensa_posible == True: break
            elif user._aumentar_defensa_posible == False: continue
        elif accion == "3":
            user.habilidad_especial(enemigo6)
            if user._habilidad_posible == True: break
            elif user._habilidad_posible == False: continue
        else: escribir_lento("Por favor, elige una opción válida")
    if enemigo6.vida == 0: break
    print(f"El {enemigo6.nombre} contraataca")
    num = random.choice([1,2])
    if num == 1:
        enemigo6.atacar(user)
    elif num == 2:
        enemigo6.habilidad_especial(user)
        if enemigo6._habilidad_posible == False: enemigo6.atacar(user)
    if user.vida == 0: 
        escribir_lento("Es triste pero, tu aventura llegó a su fin... Hasta nunca viajero.")
        juego = False
        break
user.aumentar_defensa(False)
if juego == False: exit()

escribir_lento("Viajero, dejame felicitarse por el logro conseguido. Sin embargo, en este mundo pocos tienen tiempo para disfrutar. Derrotaste al jefe pero sigues rodeado de enemigos...")
time.sleep(2)
escribir_lento("Ninguno se está moviendo. ¿Qué está pasando? Ellos se ven tan... ¿confudidos? ¿asombrados? Desde esta distancia es dificil de distinguir, y más aún si estás contucionado, sangrando, y de pie solo porque no cuentas con la suficiente fuerza para dejarte caer.")
escribir_lento("Uno de ellos comienza a caminar hacia ti, muy lentamente. En cuanto le clavas la mirada, se frena en seco, y te da la sensación de que se prepara para huir. Te concentras en recuperar el aire, no sabes qué está a punto de pasar. En el transcurso de un minuto, se fue relajando poco a poco hasta retomar su marcha. Tenía un caminar tosco, rengueaba un poco sumado a que parecía no querer acercarse, pero lo estaba haciendo. Su túnica, que iba barriendo el piso detrás suyo, tampoco ayudaba.")
escribir_lento("Era de menor altura que los guardias, o eso parecía de lejos. A medida que se acerca, distingues que es una pronunciada joroba lo que lo hace ver así, y comienzas a distinguir otros rasgos que denotan vejez. Sin bajar la guardia, lo dejas acercarse. Se frena a unos 5 metros tuyo, y ves más de cerca su vestimenta. Esto ya lo habías visto antes: es el sacerdote. Escuchas: ´Por favor, déjanos en paz´")
time.sleep(1)
escribir_lento("¿Qué? ¿Cómo? ´A esta altura ya estoy alucinando´ piensas. Tu expresión cambió notablemente, por lo que el sacerdote repitió: ´Por favor, déjanos en paz´ Podías estar alucinando una vez, pero dos ya no. ¿Te habló en tu idioma? Si, eso pasó. Los sacerdotes son los mas cultos de cada ciudad, es una regla general. Suelen tener amplios conocimientos en variadas materias, una de ellas, idiomas, ya que, en la mayoría de los lugares, están presentes todas las negociaciones que se hacen en nombre de su ciudad, o pueblo, o lo que sea, además de ser consejeros directos de los gobernantes.")
escribir_lento("Tenía todo el sentido del mundo que pueda comunicarse contigo, pero, tantos metros bajo tierra, ¿quién iba a decir que se mantenían tales tradiciones? No era momento de analizar las relaciones públicas del lugar o preguntarle al sacerdote si alguna vez hizo uso de su conocimiento en distintas lenguas. No tenías tiempo, y no tampoco querías estar mas ahí. Estabas en posición de exigir cosas, no obstante, sientes que cuanto más tiempo te quedes ahí, más peligro corres.")
escribir_lento("Debes responder tajante, con tono de autoridad, y sin mostrar la más mínima desesperación que pueda ser usada en tu contra. Es normal que luego de que derrotes a su jefe, estén asustados, te tengan miedo, y te quieran lejos. Hay que aprovechar este momento antes de que mermen las emociones.")
escribir_lento("Finalmente respondes, ´Está bien, ya cumplí mi cometido, guíame personalmente a la salida, y me iré´ ´Prométenos que no volverás´ ´Que los dioses me castiguen si eso pasa´ El sacerdote asiente con la cabeza, y te lleva hasta la salida...")
time.sleep(2)
escribir_lento("¡¡¡FELICIDADES VIAJERO!!! Ha finalizado tu primera aventura. Espero hayas disfrutado del viaje. Hasta la próxima.")