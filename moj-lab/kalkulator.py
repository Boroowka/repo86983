class Kalkulator:
    def dodaj(self, a, b):
        return a + b

    def odejmij(self, a, b):
        return a - b

    def mnoz(self, a, b):
        return a * b

    def dziel(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero")
        return a / b
