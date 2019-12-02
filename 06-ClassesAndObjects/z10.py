class TV():
    
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels  = []
        
    def off(self):
        self.is_on = False
        
    def on(self):
        self.is_on = True
        
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
        
    def set_channels(self, name):
        self.channels.append(name)
            
        
    def show_channels(self):
        print("LISTA KANAŁÓW:")
        for i in self.channels:
            print (i, end=', ')
                
    
    def show_status(self):
        if self.is_on == False:
            print('Telewizor jest wyłączony')
        elif:
            if slef.channel_no < len(self.channels):
        else:
            print(f'Telewizor jest załączony, kanał {self.channel_no}')

            
tv = TV()
tv.show_status()
tv.on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.off()
tv.show_status()
tv.set_channels('TVP1')
tv.set_channels('TVP2')
tv.set_channels('Polsat')
tv.set_channels('TVN')
tv.set_channels('Filmbox')
tv.show_channels()