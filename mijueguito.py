import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aventura de Supervivencia")

# Configuración de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Carga de imágenes
img_beach = pygame.image.load("playa.png")
img_jungle = pygame.image.load("Selva.png")
img_fruits = pygame.image.load("food.png")
img_fish = pygame.image.load("peces.png")
img_shelter = pygame.image.load("cueva.png")
img_water = pygame.image.load("agua.png")
img_cover = pygame.image.load("cover1.png") 

# Escalado de imágenes
img_beach = pygame.transform.scale(img_beach, (WIDTH, HEIGHT))
img_jungle = pygame.transform.scale(img_jungle, (WIDTH, HEIGHT))
img_fruits = pygame.transform.scale(img_fruits, (WIDTH, HEIGHT))
img_fish = pygame.transform.scale(img_fish, (WIDTH, HEIGHT))
img_shelter = pygame.transform.scale(img_shelter, (WIDTH, HEIGHT))
img_water = pygame.transform.scale(img_water, (WIDTH, HEIGHT))
img_cover = pygame.transform.scale(img_cover, (WIDTH, HEIGHT))

# Configuración de fuentes
font = pygame.font.Font(None, 36)

# Función para mostrar texto
def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

# Función para mostrar la pantalla de estado
def show_state(state):
    screen.fill(WHITE)
    if state == "start":
        screen.blit(img_cover, (0, 0))
        draw_text("Naomi es una joven aventurera que, tras un naufragio, se encuentra sola", 30, 300)
        draw_text("en una isla desierta. Desorientada, despierta en una playa de arena blanca", 30, 330)
        draw_text("rodeada de selva espesa. Con el eco de la tormenta aún resonando en sus oídos,", 30, 360)
        draw_text("comienza a explorar la isla, enfrentándose a desafíos y peligros mientras", 30, 390)
        draw_text("busca una manera de sobrevivir y, eventualmente, regresar a casa", 30 , 420)
        draw_text("1. Explorar la playa", 50, 550)
        draw_text("2. Adentrarse en la jungla", 50, 600)
    elif state == "beach":
        screen.blit(img_beach, (0, 0))
        draw_text("Bien! llegaste a la playa, el viento está lo suficientemente", 50, 150)
        draw_text("fuerte cómo para no dejarte ver, Que prefieres hacer?", 50, 170)
        draw_text("1. Buscar comida", 50, 300)
        draw_text("2. Construir un refugio", 50, 340)
    elif state == "find_food":
        screen.blit(img_fruits, (0, 0))
        draw_text("Buena opción, es necesario conservar energia, no sabes", 50, 100)
        draw_text("cuanto tiempo pasaras aqui ¿Qué tipo de comida buscas?", 50, 130 )
        draw_text("1. Buscar frutas en los arboles", 50, 160)
        draw_text("2. Buscar agua para pescar", 50, 210)
    elif state == "find_fruits":
        draw_text("Guardas las frutas y sobrevives", 50, 50)
    elif state == "fish":
        screen.blit(img_fish, (0, 0))
        draw_text("Pescar con trampa y sobrevives", 50, 100)
    elif state == "build_shelter":
        screen.blit(img_shelter, (0, 0))
        draw_text("Construyes una cabaña y te rescatan", 50, 100)
    elif state == "jungle":
        screen.blit(img_jungle, (0, 0))
        draw_text("¿Qué prefieres hacer primero?", 50, 100)
        draw_text("1. Seguir un sendero", 50, 150)
        draw_text("2. Buscar una fuente de agua", 50, 200)
    elif state == "follow_path":
        draw_text("¿Qué decides hacer?", 50, 100)
        draw_text("1. Cazar un animal", 50, 150)
        draw_text("2. Seguir las huellas hasta una fuente de agua", 50, 200)
    elif state == "hunt_animal":
        draw_text("Intentas cazar y mueres", 50, 50)
    elif state == "find_water_source":
        screen.blit(img_water, (0, 0))
        draw_text("Encuentras una fuente de agua y sobrevives", 50, 100)
    elif state == "find_water":
        draw_text("Encuentras una civilización caníbal y mueres", 50, 50)
    pygame.display.flip()

# Función para mostrar preguntas
def ask_question(question):
    screen.fill(WHITE)
    draw_text(question, 50, 250)
    draw_text("1. Sí", 50, 300)
    draw_text("2. No", 50, 350)
    pygame.display.flip()

# Función principal del juego
def game():
    # Estado inicial
    state = "start"

    # Preguntas antes del final
    questions = [
        "¿Te gusta explorar?",
        "¿Tienes miedo a la oscuridad?",
        "¿Prefieres el calor o el frío?",
        "¿Eres bueno construyendo cosas?",
        "¿Te gustan los animales salvajes?"
    ]
    random.shuffle(questions)

    # Bucle principal
    question_counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if state == "start":
                        state = "beach"
                    elif state == "beach":
                        state = "find_food"
                    elif state == "find_food":
                        state = "find_fruits"
                    elif state == "jungle":
                        state = "follow_path"
                    elif state == "follow_path":
                        state = "hunt_animal"
                elif event.key == pygame.K_2:
                    if state == "start":
                        state = "jungle"
                    elif state == "beach":
                        state = "build_shelter"
                    elif state == "find_food":
                        state = "fish"
                    elif state == "jungle":
                        state = "find_water"
                    elif state == "follow_path":
                        state = "find_water_source"
        
        if state == "start" and question_counter < len(questions):
            ask_question(questions[question_counter])
            question_counter += 1
        else:
            show_state(state)

        pygame.display.flip()

# Iniciar el juego
game()
