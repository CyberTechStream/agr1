import socket
import time
from random import randint
from threading import Thread

# Налаштування сервера
HOST = 'localhost'
PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)
sock.setblocking(False)

# Дані гравця
# ключ <socket.socket>: {id, x, y, r, name}
players = {}
id_counter = 0


def handle_data():
    while True:
        time.sleep(0.01)
        
        # гравці, від яких отрим. актуал. дані про позицію
        player_data = {}
        
        # кого з'їли
        eliminated = []
        # видалити бо з'їли або завіс
        to_remove = []
       
        for conn in list(players):
            try:
                # постійн. отрим. актуал. дані про гравців
                pass
                        
                        
            except:
                continue
       
        
        for conn1 in player_data:
            # перевірити чи з'їли когось
            
            
                
                
                
                dx = p1['x'] - p2['x']
                dy = p1['y'] - p2['y']
                distance = (dx**2 + dy**2)**0.5
                
                # відстан. від центр p1 до центр. p2 менша за радіус p1
                # та p1 більший на 10%, 
                # ТОДІ p1 -> з'їв p2 
                if distance < p1['r'] and p1['r'] > p2['r'] * 1.1:
                    players[conn1]['r'] += int(p2['r'] * 0.5)
                    eliminated.append(conn2)


        # перебрат. всіх гравців
        for conn in list(players.keys()):
            
            # якщо з'їли - відправ. LOSE +видаляємо
            
            
            
            
            # усім живим відправ. коорд. всіх гравц. 
            try:
                packet = '|'.join([f"{p['id']},{p['x']},{p['y']},{p['r']},{p['name']}"
                                 for c, p in players.items() if c != conn and c not in eliminated]) + '|'
                conn.send(packet.encode())
            except:
                to_remove.append(conn)


        # видал. хто завіс/з'їли
        
            


Thread(target=handle_data, daemon=True).start()
print(f"[SERVER] Agario server is running on {HOST}:{PORT}")


while True:
    try:
        # спавн гравця
        pass
        
    except:
        pass
