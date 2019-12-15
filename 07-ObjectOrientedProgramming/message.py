class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        self.message = message
        self.message = self.message.capitalize() + ' BYE.'
    def __str__(self):
        return self.message