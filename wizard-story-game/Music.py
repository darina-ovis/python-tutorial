from pgzero import tone


class Music:
    def __init__(self, clock):
        self.tone = None
        self.melody = 'D4 C4 D4 E4 F4 E4 D4 C4 D4 C4 B3 C4 A3 A4 G4 A4 B4 C5 B4 A4 G4 A4 B4 C5 D5 E5'.split(' ')
        self.clock = clock

    def play(self):
        delay = 1.0
        for note in self.melody:
            self.tone = tone.create(note, 1)
            self.clock.schedule(self.play_one_note, delay)
            delay += 1.0

    def play_one_note(self):
        self.tone.play()
