class Countre:

    def __init__(self, c):
        self.c = c
    def count(self):
        d = len(self.c)
        return d

    def count_word(self):
        recount = 0
        for e in self.c:
           if e == " ":
                recount = 1
        print(recount + 1)

    def print(self):
        print(self.c)


mycounter = Countre("hello world")
mycounter.count_word()
print(mycounter.count())

