from multiprocessing import Process

from pgzero import tone
from pygame import time


class Music:
    def __init__(self):
        self.tones = []
        self.melody = 'D4 C4 D4 E4 F4 E4 D4 C4 D4 C4 B3 C4 A3 A4 G4 A4 B4 C5 B4 A4 G4 A4 B4 C5 D5 E5'.split(' ')
        for note in self.melody:
            self.tones.append(tone.create(note, 0.4))

    def play(self):
        for i, sound in enumerate(self.tones):
            channel = sound.play()
            while channel.get_busy():
                if channel.get_queue() is None:
                    i += 1
                    if i >= len(self.tones):
                        return
                    channel.queue(self.tones[i])