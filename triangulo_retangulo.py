"""
Escreva, na classe Triangulo, o método retangulo() que devolve True se o triângulo for retângulo, e False caso contrário.

Exemplos:
t = Triangulo(1, 3, 5)
t.retangulo()
# deve devolver False

u = Triangulo(3, 4, 5)
u.retangulo()
# deve devolver True
"""

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
            return ""
    
    def retangulo(self)-> bool:
        hip = self.a
        resultado = self.tipo_lado()
        if resultado == "":

            if hip < self.b:
                hip = self.b 
            if hip < self.c:
                hip = self.c

            if hip == self.b:
                if hip ** 2 == self.a ** 2 + self.c ** 2:
                    return True
                else: 
                    return False
            elif hip == self.a:
                if hip ** 2 == self.b ** 2 + self.c ** 2:
                    return True
                else: 
                    return False
            elif hip == self.c:
                if hip ** 2 == self.a ** 2 + self.b ** 2:
                    return True
                else: 
                    return False
            else:
                return False


        else:
            return False

