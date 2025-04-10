class Card:
    def __init__(self, suit, value, face_up = False):
        self.suit = suit
        self.value = value
        self.face_up = face_up

    def rotate(self):
        self.face_up = not self.face_up

    def __str__(self):
        return f"{self.suit}{self.value}" if self.face_up else "XX"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit and self.value == other.value