# TV.py
# Mimics turning a TV on and off, etc.

class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = 1
        
    def turnOn(self):
        self.on = True
    
    def turnOff(self):
        self.on = True
        
    def getChannel(self):
        return self.channel
    
    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel
    
    def getVolumeLevel(self):
        return self.volume
    
    def setVolumeLevel(self, volume):
        if self.on and 1 <= volume <= 7:
            self.volume = volume
            
    def channelUp(self):
        if self.on:
            if self.channel < 120:
                self.channel += 1
            else:
                self.channel = 1
                
    def channelDown(self):
        if self.on:
            if self.channel > 1:
                self.channel -= 1
            else:
                self.channel = 120
                
    def volumeUp(self):
        if self.on:
            if self.volume < 7:
                self.volume += 1
                
    def volumeDown(self):
        if self.on:
            if self.volume > 1:
                self.volume -= 1