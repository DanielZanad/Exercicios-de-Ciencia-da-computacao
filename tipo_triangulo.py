class Triangulo:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self)-> str:
        if self.a == self.b and self.c == self.b:
            return "equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isósceles"
        else:
            return "escaleno"

t = Triangulo(3,4,5)
print(t.tipo_lado())