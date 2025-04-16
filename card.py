class Card:
    def __init__(self, suit, value, face_up = False):
        self.suit = suit
        self.value = value
        self.face_up = face_up

    def rotate(self):
        self.face_up = not self.face_up

    def __str__(self):
        suit = self.suit.replace('\uFE0F', '')
        return f"{suit}{self.value}" if self.face_up else "xx"