from customtkinter import *

class ConnectWindow(CTk):
    def __init__(self):
        super().__init__()

        self.name = "Test"
        self.host = "localhost"
        self.port = 8080

        self.title('Agario Launcher')
        self.geometry('300x400')
        
        # Головний напис
       
        
        # Поля для введення ніку, хост, порт
        

        # Кнопка 'Приєднатися'
        



    # Фунція створення поля для введення даних
    def make_entry(self, placeholder):
        entry = CTkEntry(self, placeholder_text=placeholder, height=50)
        entry.pack(padx=20, pady=5, fill="x")
        return entry
    
    # Витягнути дані та закрити вікно лаунчера
    def open_game(self):
        pass
