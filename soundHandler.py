import os
import simpleaudio as sa


class soundHandler():
    def __init__(self, game):
        self.game = game
        self.playObject = None
        self.waveObject = None


    
    def playSound(self, filename):

        currentDir = os.getcwd()
        filename = currentDir.replace('\\', '/')+'/sounds/'+filename

        wave_obj = sa.WaveObject.from_wave_file(filename)
        wave_obj.play()
        

    def startMusic(self, filename):
        currentDir = os.getcwd()
        filename = currentDir.replace('\\', '/')+'/sounds/'+filename

        self.waveObject = sa.WaveObject.from_wave_file(filename)
        self.playObject = self.waveObject.play()

    def draw(self):
        pass

    def update(self):
        if not self.playObject.is_playing():
            self.playObject = self.waveObject.play()




if __name__ == '__main__':
    soundHandlerInit = soundHandler('test')
    soundHandlerInit.playSound('gunshot2.wav')
