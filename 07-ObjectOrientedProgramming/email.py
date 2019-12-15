from message import Message

class Email(Message):
    
    def __init__(self, adres_nadawcy, adres_odbiorcy, temat):
        self.adres_nadawcy = adres_nadawcy
        self.adres_odbiorcy = adres_odbiorcy
        self.temat = temat
    
    def send(self, message):
        super().set_message(message)
        print(f'''Od: {self.adres_nadawcy}
Do: {self.adres_odbiorcy}
Temat: {self.temat}
Treść: {self.message}''')