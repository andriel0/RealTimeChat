import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog


class Chat:
    def __init__(self):
        HOST = '127.0.0.1'
        PORT = 55555
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

        login = Tk()
        login.withdraw()
        self.loaded_window = False
        self.active = True

        self.name = simpledialog.askstring('Nome', 'Digite seu nome: ', parent=login)
        self.room = simpledialog.askstring('Sala', 'Digite o nome da sala: ', parent=login)

        thread = threading.Thread(target=self.connect)
        thread.start()
        self.window()

    def window(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title('Chat')

        self.text_box = Text(self.root)
        self.text_box.place(relx=0.05, rely=0.01, width=700, height=600)

        self.msg_box = Entry(self.root)
        self.msg_box.place(relx=0.05, rely=0.8, width=500, height=20)

        self.btn_send = Button(self.root, text='Enviar', command=self.sendMessageToChat)
        self.btn_send.place(relx=0.7, rely=0.8, width=100, height=20)
        self.root.protocol('WM_DELETE_WINDOW', self.closeWindow)

        self.root.mainloop()

    def closeWindow(self):
        self.root.destroy()
        self.client.close()

    def connect(self):
        while True:
            received = self.client.recv(1024)
            if received == b'SALA':
                self.client.send(self.name.encode())
                self.client.send(self.room.encode())
            else:
                try:
                    self.text_box.insert('end', received.decode())
                except:
                    pass

    def sendMessageToChat(self):
        message = self.msg_box.get()
        self.msg_box.delete(0, 'end')
        self.client.send(message.encode())


chat = Chat()
