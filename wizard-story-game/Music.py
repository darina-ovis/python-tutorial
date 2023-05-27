import pgzero.tone

from pgzero import tone
from pygame import time


class Music:
    def __init__(self, clock):
        self.tones = []
        self.melody = 'D4 C4 D4 E4 F4 E4 D4 C4 D4 C4 B3 C4 A3 A4 G4 A4 B4 C5 B4 A4 G4 A4 B4 C5 D5 E5'.split(' ')
        for note in self.melody:
            self.tones.append(tone.create(note, 1))
            tone.note_queue.put(tone._convert_args(note, 1))
        # self.channel = self.tones[0].play()
        self.clock = clock

    def play(self):
        channel = self.tones[0].play()
        channel.queue(self.tones[1])
        channel.get_queue(self.tones[2])
        # for sound in self.tones:
        #     channel.queue(sound)
        #     clock.tick(sound.get_length())
