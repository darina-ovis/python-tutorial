class Countre:

    def __init__(self, c):
        self.c = c

    def vowels(self):
        vowels = ["a", "e", "y", "u", "i", "o"]
        vowels_count = 0
        for char in self.c:
            if char.lower() in vowels:
                vowels_count += 1
        return vowels_count

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


mycounter = Countre(input())
mycounter.vowels()
print(mycounter.vowels())
