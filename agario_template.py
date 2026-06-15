from pygame import *
from random import randint
from pygame.math import Vector2
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

from menu import ConnectWindow

# Лаунчер




# Сокет
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((host, port))

my_data = list(map(int, sock.recv(64).decode().strip().split(',')))
my_id = my_data[0]
my_player = my_data[1:] # [x, y, radius, nick]
sock.setblocking(False)

init()

# Налаштування
window = display.set_mode((1000, 1000))
clock = time.Clock()
lose_font = font.Font(None, 50)
nick_font = font.Font(None, 20)

# розмір карти
MAP_SIZE = 2000
# швидк. гравця
PLAYER_SPEED = 15
# кількість їжі на карті
FOOD_COUNT = 300


running = True
lose = False
all_players = []


def receive_data():
    global all_players, running, lose
    # отримуємо дані від сервера
    

# клас Food


# спавн їжі на карті
foods = []




# функція малювання кола
def draw_circle(x, y, r, color, name=None):
    sx = int((x - my_player[0]) * scale + 500)
    sy = int((y - my_player[1]) * scale + 500)

    draw.circle(window, color, (sx, sy), int(r * scale))

    if name:
        nick = nick_font.render(name, True, (0, 0, 0))
        window.blit(nick, (sx-nick.get_rect().width//2, sy-nick.get_rect().height//2))
        
        
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    
    # Масштаб залежно від розміру гравця, але діапазон між 0.3 і 1.5
    # маленький гравець → великий scale → камера наближена;
    # великий гравець → маленький scale → камера віддаляється.
    
    
    
    
    # якщо не програв
    


        # ОБМЕЖЕННЯ КАРТИ
        my_player[0] = max(-MAP_SIZE, min(MAP_SIZE, my_player[0]))
        my_player[1] = max(-MAP_SIZE, min(MAP_SIZE, my_player[1]))
    
    
    window.fill((255, 255, 255))
    
    # Рамка навколо карти
    border_size = int(MAP_SIZE * scale)
    draw.rect(window, (0, 0, 0), 
        (
            int((-MAP_SIZE - my_player[0]) * scale + 500),
            int((-MAP_SIZE - my_player[1]) * scale + 500),
            border_size * 2,
            border_size * 2
        ), 3)


    # малюємо нашого гравця
    


    # Інші гравці
        
        # себе пропускаємо
        
        
        # коло інших гравців
        





    # рендер їжі
        
        # якщо торкнув. їжу
            
            # +маса = 20% від маси їжі
            
        
            # рендер їжі
            


    # текст якщо програв

    
    
    
    
    # Спавн нової їжі






    display.update()
    clock.tick(60)
quit()