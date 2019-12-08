class TV():
    
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels  = []
        self.volume = 0
        
    def off(self):
        self.is_on = False
        
    def on(self):
        self.is_on = True
        
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
        
    def set_channels(self, name):
        self.channels.append(name)
        
    def turn_up(self):
        if self.volume < 10:
            self.volume += 1
            
    def turn_down(self):
        if self.volume > 0:
            self.volume -= 1
        
    def show_channels(self):
        print("LISTA KANAŁÓW:")
        for i in self.channels:
            print (i, end=', ')
        print('')
                
    
    def show_status(self):
        if self.is_on == False:
            print('Telewizor jest wyłączony')
        elif self.channel_no <= len(self.channels) and self.is_on == True:
            x = self.channel_no - 1
            print(f'Telewizor jest załączony, kanał {self.channel_no} ({self.channels[x]})')
            print(f'Poziom głośności: {self.volume}')
        else:
            print(f'Telewizor jest załączony, kanał {self.channel_no}')
            print(f'Poziom głośności: {self.volume}')