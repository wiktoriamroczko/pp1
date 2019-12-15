from message import Message

class SMS(Message):
    
    def __init__(self,nr_nadawcy,nr_odbiorcy):
        self.nr_nadawcy = nr_nadawcy
        self.nr_odbiorcy = nr_odbiorcy
        super().__init__()
        
    def send(self,message):
        super().set_message(message)
        print(f'''Od: {self.nr_nadawcy}
Do: {self.nr_odbiorcy}
Treść: {self.message}''')