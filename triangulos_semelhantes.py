"""
Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve devolver True. Caso negativo, deve devolver False

Um triângulo é semelhante a outro triângulo se a razão (divisão) entre os comprimentos dos seus lados forem iguais.

Dica: você pode colocar os lados de cada um dos triângulos em uma lista diferente e ordená-las.

Exemplo:
t1 = Triangulo(2, 3, 5)
t2 = Triangulo(4, 6, 10)
t1.semelhantes(t2)
# deve devolver True
"""
class Triangulo:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self, a, b, c)-> str:
        if a == b and c == b:
            return "equilátero"
        elif a == b or self.a == c or b == c:
            return "isósceles"
        else:
            return "escaleno"

    def semelhantes(self, obj: object)-> bool:
        resultado = self.tipo_lado(obj.a,obj.b,obj.c)
        resultado1 = self.tipo_lado(self.a, self.b, self.c)
        if resultado == resultado1:
            return True
        else:
            return False

